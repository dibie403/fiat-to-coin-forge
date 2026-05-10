export const formatNGN = (n: number) =>
  new Intl.NumberFormat("en-NG", {
    style: "currency",
    currency: "NGN",
    maximumFractionDigits: 0,
  }).format(n);

export const formatCrypto = (n: number, symbol: string) =>
  `${n.toLocaleString(undefined, { maximumFractionDigits: 8 })} ${symbol}`;

export const formatDate = (iso: string) =>
  new Date(iso).toLocaleString(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  });
