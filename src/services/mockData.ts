export interface Crypto {
  symbol: string;
  name: string;
  rate: number; // NGN per unit
  change24h: number;
  image?: string;
  marketCap?: number;
  volume24h?: number;
  high24h?: number;
  low24h?: number;
  circulatingSupply?: number;
  totalSupply?: number;
  maxSupply?: number | null;
  ath?: number;
  athDate?: string;
  atl?: number;
  atlDate?: string;
  sparkline7d?: number[];
  rank?: number;
}

export interface User {
  id: string;
  name: string;
  email: string;
  password: string;
  role: "user" | "admin";
}

export type TxType = "BUY" | "SELL";
export type TxStatus =
  | "PENDING_PAYMENT"
  | "PAID"
  | "PENDING_ADMIN_CONFIRMATION"
  | "COMPLETED"
  | "FAILED";

export interface Transaction {
  id: string;
  userId: string;
  userEmail: string;
  type: TxType;
  crypto: string;
  fiatAmount: number;
  cryptoAmount: number;
  walletAddress: string;
  status: TxStatus;
  timestamp: string;
}

export const initialRates: Crypto[] = [
  { symbol: "BTC", name: "Bitcoin", rate: 65_000_000, change24h: 2.34 },
  { symbol: "ETH", name: "Ethereum", rate: 4_200_000, change24h: -1.12 },
  { symbol: "USDT", name: "Tether", rate: 1_550, change24h: 0.05 },
];

export const seedUsers: User[] = [
  { id: "u-admin", name: "Admin", email: "admin@brokr.io", password: "admin123", role: "admin" },
  { id: "u-demo", name: "Demo User", email: "demo@brokr.io", password: "demo123", role: "user" },
];

export const ADMIN_WALLETS: Record<string, string> = {
  BTC: "bc1qbrokrxadminxwalletxxxxxxxxxxxxxxxxxxx",
  ETH: "0xBR0KR0AdM1n0WaLLet0000000000000000000001",
  USDT: "TBrokrAdminUSDTWalletAddressXXXXXXXX",
};
