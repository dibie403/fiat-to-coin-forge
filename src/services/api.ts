/**
 * Mock API service layer.
 * Swap implementations here to integrate a real Django backend later.
 * All functions return Promises and simulate latency.
 */
import {
  ADMIN_WALLETS,
  initialRates,
  seedUsers,
  type Crypto,
  type Transaction,
  type TxStatus,
  type User,
} from "./mockData";

const LS = {
  users: "brokr.users",
  rates: "brokr.rates",
  txs: "brokr.txs",
  session: "brokr.session",
};

const isBrowser = () => typeof window !== "undefined";

const delay = (ms = 350) => new Promise((r) => setTimeout(r, ms));

function read<T>(key: string, fallback: T): T {
  if (!isBrowser()) return fallback;
  try {
    const raw = localStorage.getItem(key);
    return raw ? (JSON.parse(raw) as T) : fallback;
  } catch {
    return fallback;
  }
}

function write<T>(key: string, value: T) {
  if (!isBrowser()) return;
  localStorage.setItem(key, JSON.stringify(value));
}

function ensureSeed() {
  if (!isBrowser()) return;
  if (!localStorage.getItem(LS.users)) write(LS.users, seedUsers);
  if (!localStorage.getItem(LS.rates)) write(LS.rates, initialRates);
  if (!localStorage.getItem(LS.txs)) write(LS.txs, []);
}

ensureSeed();

const uid = () => Math.random().toString(36).slice(2, 10);

// ---------- AUTH ----------
export interface AuthResult {
  token: string;
  user: Omit<User, "password">;
}

export async function registerUser(input: {
  name: string;
  email: string;
  password: string;
}): Promise<AuthResult> {
  await delay();
  const users = read<User[]>(LS.users, []);
  if (users.find((u) => u.email.toLowerCase() === input.email.toLowerCase())) {
    throw new Error("Email already registered");
  }
  const user: User = {
    id: "u-" + uid(),
    name: input.name,
    email: input.email,
    password: input.password,
    role: "user",
  };
  users.push(user);
  write(LS.users, users);
  const { password: _p, ...safe } = user;
  const session = { token: "mock-jwt-" + user.id, user: safe };
  write(LS.session, session);
  return session;
}

export async function loginUser(input: {
  email: string;
  password: string;
}): Promise<AuthResult> {
  await delay();
  const users = read<User[]>(LS.users, []);
  const u = users.find(
    (x) =>
      x.email.toLowerCase() === input.email.toLowerCase() &&
      x.password === input.password,
  );
  if (!u) throw new Error("Invalid credentials");
  const { password: _p, ...safe } = u;
  const session = { token: "mock-jwt-" + u.id, user: safe };
  write(LS.session, session);
  return session;
}

export function logout() {
  if (!isBrowser()) return;
  localStorage.removeItem(LS.session);
}

export function getSession(): AuthResult | null {
  return read<AuthResult | null>(LS.session, null);
}

export async function listUsers(): Promise<Omit<User, "password">[]> {
  await delay(150);
  return read<User[]>(LS.users, []).map(({ password: _p, ...rest }) => rest);
}

// ---------- RATES ----------
const COINGECKO_IDS: Record<string, string> = {
  BTC: "bitcoin",
  ETH: "ethereum",
  USDT: "tether",
};
const LS_OVERRIDES = "brokr.rate_overrides";

function readOverrides(): Record<string, number> {
  return read<Record<string, number>>(LS_OVERRIDES, {});
}

interface MarketRow {
  id: string;
  symbol: string;
  name: string;
  image: string;
  current_price: number;
  market_cap: number;
  market_cap_rank: number;
  total_volume: number;
  high_24h: number;
  low_24h: number;
  price_change_percentage_24h: number;
  circulating_supply: number;
  total_supply: number | null;
  max_supply: number | null;
  ath: number;
  ath_date: string;
  atl: number;
  atl_date: string;
  sparkline_in_7d?: { price: number[] };
}

async function fetchLiveMarkets(): Promise<Record<string, MarketRow> | null> {
  try {
    const ids = Object.values(COINGECKO_IDS).join(",");
    const url = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=ngn&ids=${ids}&order=market_cap_desc&sparkline=true&price_change_percentage=24h`;
    const res = await fetch(url);
    if (!res.ok) return null;
    const data = (await res.json()) as MarketRow[];
    const out: Record<string, MarketRow> = {};
    for (const [sym, id] of Object.entries(COINGECKO_IDS)) {
      const row = data.find((d) => d.id === id);
      if (row) out[sym] = row;
    }
    return out;
  } catch {
    return null;
  }
}

export interface CoinChartPoint { t: number; price: number; }
export async function getCoinChart(symbol: string, days = 7): Promise<CoinChartPoint[]> {
  const id = COINGECKO_IDS[symbol];
  if (!id) return [];
  try {
    const url = `https://api.coingecko.com/api/v3/coins/${id}/market_chart?vs_currency=ngn&days=${days}`;
    const res = await fetch(url);
    if (!res.ok) return [];
    const data = (await res.json()) as { prices: [number, number][] };
    return data.prices.map(([t, price]) => ({ t, price }));
  } catch {
    return [];
  }
}

export async function getRates(): Promise<Crypto[]> {
  const stored = read<Crypto[]>(LS.rates, initialRates);
  const overrides = readOverrides();
  const live = await fetchLiveMarkets();
  const merged = stored.map((r) => {
    const row = live?.[r.symbol];
    if (row) {
      // Live data ALWAYS wins. Overrides are ignored when CoinGecko responds.
      return {
        ...r,
        rate: row.current_price,
        change24h: Number((row.price_change_percentage_24h ?? 0).toFixed(2)),
        image: row.image,
        marketCap: row.market_cap,
        volume24h: row.total_volume,
        high24h: row.high_24h,
        low24h: row.low_24h,
        circulatingSupply: row.circulating_supply,
        totalSupply: row.total_supply ?? undefined,
        maxSupply: row.max_supply,
        ath: row.ath,
        athDate: row.ath_date,
        atl: row.atl,
        atlDate: row.atl_date,
        sparkline7d: row.sparkline_in_7d?.price,
        rank: row.market_cap_rank,
      } satisfies Crypto;
    }
    // Live API failed — fall back to admin override, then last cached value.
    return {
      ...r,
      rate: overrides[r.symbol] ?? r.rate,
    };
  });
  write(LS.rates, merged);
  return merged;
}

export async function updateRate(symbol: string, rate: number): Promise<Crypto[]> {
  await delay();
  const overrides = readOverrides();
  overrides[symbol] = rate;
  write(LS_OVERRIDES, overrides);
  const rates = read<Crypto[]>(LS.rates, initialRates);
  const next = rates.map((r) => (r.symbol === symbol ? { ...r, rate } : r));
  write(LS.rates, next);
  return next;
}

export async function clearRateOverride(symbol: string): Promise<void> {
  const overrides = readOverrides();
  delete overrides[symbol];
  write(LS_OVERRIDES, overrides);
}

export function getStoredRates(): Crypto[] {
  return read<Crypto[]>(LS.rates, initialRates);
}

// ---------- TRANSACTIONS ----------
export async function createBuyOrder(input: {
  userId: string;
  userEmail: string;
  crypto: string;
  fiatAmount: number;
  cryptoAmount: number;
  walletAddress: string;
}): Promise<Transaction> {
  await delay();
  const tx: Transaction = {
    id: "tx-" + uid(),
    userId: input.userId,
    userEmail: input.userEmail,
    type: "BUY",
    crypto: input.crypto,
    fiatAmount: input.fiatAmount,
    cryptoAmount: input.cryptoAmount,
    walletAddress: input.walletAddress,
    status: "PENDING_PAYMENT",
    timestamp: new Date().toISOString(),
  };
  const txs = read<Transaction[]>(LS.txs, []);
  txs.unshift(tx);
  write(LS.txs, txs);
  return tx;
}

export async function createSellOrder(input: {
  userId: string;
  userEmail: string;
  crypto: string;
  fiatAmount: number;
  cryptoAmount: number;
  walletAddress: string; // admin wallet user is sending to
}): Promise<Transaction> {
  await delay();
  const tx: Transaction = {
    id: "tx-" + uid(),
    userId: input.userId,
    userEmail: input.userEmail,
    type: "SELL",
    crypto: input.crypto,
    fiatAmount: input.fiatAmount,
    cryptoAmount: input.cryptoAmount,
    walletAddress: input.walletAddress,
    status: "PENDING_ADMIN_CONFIRMATION",
    timestamp: new Date().toISOString(),
  };
  const txs = read<Transaction[]>(LS.txs, []);
  txs.unshift(tx);
  write(LS.txs, txs);
  return tx;
}

export async function updateTransactionStatus(
  id: string,
  status: TxStatus,
): Promise<Transaction> {
  await delay();
  const txs = read<Transaction[]>(LS.txs, []);
  const idx = txs.findIndex((t) => t.id === id);
  if (idx === -1) throw new Error("Transaction not found");
  txs[idx] = { ...txs[idx], status };
  write(LS.txs, txs);
  return txs[idx];
}

export async function getUserTransactions(userId: string): Promise<Transaction[]> {
  await delay(150);
  return read<Transaction[]>(LS.txs, []).filter((t) => t.userId === userId);
}

export async function getAdminOrders(): Promise<Transaction[]> {
  await delay(150);
  return read<Transaction[]>(LS.txs, []);
}

export function getAdminWallet(symbol: string): string {
  return ADMIN_WALLETS[symbol] ?? "N/A";
}
