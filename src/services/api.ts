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
export async function getRates(): Promise<Crypto[]> {
  await delay(200);
  // simulate small live fluctuation
  const rates = read<Crypto[]>(LS.rates, initialRates).map((r) => ({
    ...r,
    rate: Math.round(r.rate * (1 + (Math.random() - 0.5) * 0.002)),
  }));
  return rates;
}

export async function updateRate(symbol: string, rate: number): Promise<Crypto[]> {
  await delay();
  const rates = read<Crypto[]>(LS.rates, initialRates);
  const next = rates.map((r) => (r.symbol === symbol ? { ...r, rate } : r));
  write(LS.rates, next);
  return next;
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
