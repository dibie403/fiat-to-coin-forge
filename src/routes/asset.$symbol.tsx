import { createFileRoute, Link, useParams } from "@tanstack/react-router";
import { useEffect, useMemo, useState } from "react";
import { ArrowDownRight, ArrowUpRight, TrendingDown, TrendingUp } from "lucide-react";
import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { Header } from "@/components/Header";
import { Button } from "@/components/ui/button";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import { getCoinChart, getRates, type CoinChartPoint } from "@/services/api";
import type { Crypto } from "@/services/mockData";
import { formatCompact, formatCompactNGN, formatNGN } from "@/utils/format";

export const Route = createFileRoute("/asset/$symbol")({
  head: ({ params }) => ({
    meta: [{ title: `${params.symbol} — Orji Funds Exchange` }],
  }),
  component: AssetPage,
});

const RANGES = [
  { key: "1", label: "24h" },
  { key: "7", label: "7d" },
  { key: "30", label: "30d" },
  { key: "90", label: "90d" },
  { key: "365", label: "1y" },
] as const;

function AssetPage() {
  const { ready } = useRequireAuth();
  const { symbol } = useParams({ from: "/asset/$symbol" });
  const sym = symbol.toUpperCase();
  const [coin, setCoin] = useState<Crypto | null>(null);
  const [days, setDays] = useState<string>("7");
  const [chart, setChart] = useState<CoinChartPoint[]>([]);
  const [loadingChart, setLoadingChart] = useState(true);

  useEffect(() => {
    if (!ready) return;
    let live = true;
    const refresh = async () => {
      const rates = await getRates();
      if (!live) return;
      setCoin(rates.find((r) => r.symbol === sym) ?? null);
    };
    refresh();
    const id = setInterval(refresh, 30_000);
    return () => {
      live = false;
      clearInterval(id);
    };
  }, [ready, sym]);

  useEffect(() => {
    if (!ready) return;
    let live = true;
    setLoadingChart(true);
    getCoinChart(sym, Number(days)).then((d) => {
      if (!live) return;
      setChart(d);
      setLoadingChart(false);
    });
    return () => {
      live = false;
    };
  }, [ready, sym, days]);

  const series = useMemo(
    () => chart.map((p) => ({ t: p.t, price: p.price })),
    [chart],
  );
  const up = (coin?.change24h ?? 0) >= 0;

  if (!ready) return null;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main className="mx-auto max-w-6xl px-4 py-10 space-y-8">
        {!coin ? (
          <div className="text-muted-foreground">Loading {sym}…</div>
        ) : (
          <>
            <div className="flex flex-wrap items-end justify-between gap-6">
              <div className="flex items-center gap-4">
                {coin.image && (
                  <img src={coin.image} alt={coin.name} className="h-14 w-14 rounded-full" />
                )}
                <div>
                  <p className="text-xs uppercase tracking-wider text-muted-foreground">
                    {coin.rank ? `Rank #${coin.rank}` : "Asset"}
                  </p>
                  <h1 className="text-3xl font-bold tracking-tight">
                    {coin.name} <span className="text-muted-foreground">/ {coin.symbol}</span>
                  </h1>
                </div>
              </div>

              <div className="text-right">
                <p className="text-3xl font-bold tabular-nums">{formatNGN(coin.rate)}</p>
                <p
                  className={`inline-flex items-center gap-1 text-sm font-medium ${
                    up ? "text-primary" : "text-destructive"
                  }`}
                >
                  {up ? <TrendingUp className="h-4 w-4" /> : <TrendingDown className="h-4 w-4" />}
                  {coin.change24h > 0 ? "+" : ""}
                  {coin.change24h.toFixed(2)}% (24h)
                </p>
              </div>
            </div>

            <div className="flex gap-2">
              <Link to="/buy">
                <Button className="gap-1">
                  <ArrowDownRight className="h-4 w-4" /> Buy {coin.symbol}
                </Button>
              </Link>
              <Link to="/sell">
                <Button variant="outline" className="gap-1">
                  <ArrowUpRight className="h-4 w-4" /> Sell {coin.symbol}
                </Button>
              </Link>
            </div>

            <section className="rounded-xl border border-border bg-card p-5">
              <div className="flex items-center justify-between gap-4">
                <h2 className="text-sm font-medium uppercase tracking-wider text-muted-foreground">
                  Price chart (NGN)
                </h2>
                <div className="inline-flex rounded-lg border border-border p-1">
                  {RANGES.map((r) => (
                    <button
                      key={r.key}
                      onClick={() => setDays(r.key)}
                      className={`rounded-md px-2.5 py-1 text-xs font-medium transition ${
                        days === r.key
                          ? "bg-primary text-primary-foreground"
                          : "text-muted-foreground hover:text-foreground"
                      }`}
                    >
                      {r.label}
                    </button>
                  ))}
                </div>
              </div>

              <div className="mt-4 h-72 w-full">
                {loadingChart ? (
                  <div className="flex h-full items-center justify-center text-sm text-muted-foreground">
                    Loading chart…
                  </div>
                ) : series.length === 0 ? (
                  <div className="flex h-full items-center justify-center text-sm text-muted-foreground">
                    Chart unavailable.
                  </div>
                ) : (
                  <ResponsiveContainer width="100%" height="100%">
                    <AreaChart data={series} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                      <defs>
                        <linearGradient id="px" x1="0" y1="0" x2="0" y2="1">
                          <stop offset="0%" stopColor="oklch(0.78 0.18 150)" stopOpacity={0.45} />
                          <stop offset="100%" stopColor="oklch(0.78 0.18 150)" stopOpacity={0} />
                        </linearGradient>
                      </defs>
                      <CartesianGrid stroke="oklch(0.3 0.01 250 / 0.3)" vertical={false} />
                      <XAxis
                        dataKey="t"
                        tickFormatter={(t) =>
                          new Date(t).toLocaleDateString(undefined, {
                            month: "short",
                            day: "numeric",
                            ...(Number(days) <= 1 ? { hour: "2-digit" } : {}),
                          })
                        }
                        stroke="currentColor"
                        className="text-muted-foreground"
                        fontSize={11}
                        minTickGap={40}
                      />
                      <YAxis
                        domain={["auto", "auto"]}
                        tickFormatter={(v) => formatCompactNGN(Number(v))}
                        stroke="currentColor"
                        className="text-muted-foreground"
                        fontSize={11}
                        width={70}
                      />
                      <Tooltip
                        contentStyle={{
                          background: "oklch(0.18 0.02 250)",
                          border: "1px solid oklch(0.3 0.02 250)",
                          borderRadius: 8,
                          fontSize: 12,
                        }}
                        labelFormatter={(t) => new Date(Number(t)).toLocaleString()}
                        formatter={(v) => [formatNGN(Number(v)), "Price"]}
                      />
                      <Area
                        type="monotone"
                        dataKey="price"
                        stroke="oklch(0.78 0.18 150)"
                        strokeWidth={2}
                        fill="url(#px)"
                      />
                    </AreaChart>
                  </ResponsiveContainer>
                )}
              </div>
            </section>

            <section className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              <Stat label="Market cap" value={coin.marketCap ? formatCompactNGN(coin.marketCap) : "—"} />
              <Stat label="24h volume" value={coin.volume24h ? formatCompactNGN(coin.volume24h) : "—"} />
              <Stat label="24h high" value={coin.high24h ? formatNGN(coin.high24h) : "—"} />
              <Stat label="24h low" value={coin.low24h ? formatNGN(coin.low24h) : "—"} />
              <Stat
                label="Circulating supply"
                value={coin.circulatingSupply ? `${formatCompact(coin.circulatingSupply)} ${coin.symbol}` : "—"}
              />
              <Stat
                label="Total supply"
                value={coin.totalSupply ? `${formatCompact(coin.totalSupply)} ${coin.symbol}` : "—"}
              />
              <Stat
                label="Max supply"
                value={coin.maxSupply ? `${formatCompact(coin.maxSupply)} ${coin.symbol}` : "∞"}
              />
              <Stat
                label="All-time high"
                value={coin.ath ? formatNGN(coin.ath) : "—"}
                hint={coin.athDate ? new Date(coin.athDate).toLocaleDateString() : undefined}
              />
              <Stat
                label="All-time low"
                value={coin.atl ? formatNGN(coin.atl) : "—"}
                hint={coin.atlDate ? new Date(coin.atlDate).toLocaleDateString() : undefined}
              />
            </section>

            <p className="text-xs text-muted-foreground">
              Market data by CoinGecko · refreshes every 30s
            </p>
          </>
        )}
      </main>
    </div>
  );
}

function Stat({ label, value, hint }: { label: string; value: string; hint?: string }) {
  return (
    <div className="rounded-xl border border-border bg-card p-4">
      <p className="text-xs uppercase tracking-wider text-muted-foreground">{label}</p>
      <p className="mt-1 text-lg font-semibold tabular-nums">{value}</p>
      {hint && <p className="text-xs text-muted-foreground">{hint}</p>}
    </div>
  );
}
