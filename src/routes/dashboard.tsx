import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { ArrowDownRight, ArrowUpRight, TrendingUp, TrendingDown } from "lucide-react";
import { Area, AreaChart, ResponsiveContainer } from "recharts";
import { Header } from "@/components/Header";
import { TransactionTable } from "@/components/TransactionTable";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/context/AuthContext";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import { getRates, getUserTransactions } from "@/services/api";
import type { Crypto, Transaction } from "@/services/mockData";
import { formatCompactNGN, formatNGN } from "@/utils/format";

export const Route = createFileRoute("/dashboard")({
  head: () => ({ meta: [{ title: "Dashboard — Orji Funds Exchange" }] }),
  component: Dashboard,
});

function Dashboard() {
  const { ready } = useRequireAuth();
  const { user } = useAuth();
  const [rates, setRates] = useState<Crypto[]>([]);
  const [txs, setTxs] = useState<Transaction[]>([]);

  useEffect(() => {
    if (!ready || !user) return;
    let live = true;
    const refresh = async () => {
      const [r, t] = await Promise.all([getRates(), getUserTransactions(user.id)]);
      if (!live) return;
      setRates(r);
      setTxs(t);
    };
    refresh();
    const id = setInterval(() => getRates().then((r) => live && setRates(r)), 30_000);
    return () => {
      live = false;
      clearInterval(id);
    };
  }, [ready, user]);

  if (!ready) return null;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main className="mx-auto max-w-6xl px-4 py-10 space-y-10">
        <div className="flex flex-wrap items-end justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold tracking-tight">
              Hi, {user?.name.split(" ")[0]} 👋
            </h1>
            <p className="text-sm text-muted-foreground">
              Live rates, your wallet, and recent activity.
            </p>
          </div>
          <div className="flex gap-2">
            <Link to="/buy">
              <Button className="gap-1">
                <ArrowDownRight className="h-4 w-4" /> Buy
              </Button>
            </Link>
            <Link to="/sell">
              <Button variant="outline" className="gap-1">
                <ArrowUpRight className="h-4 w-4" /> Sell
              </Button>
            </Link>
          </div>
        </div>

        <section>
          <h2 className="mb-3 text-sm font-medium uppercase tracking-wider text-muted-foreground">
            Live rates
          </h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {rates.map((c) => {
              const up = c.change24h >= 0;
              const spark = (c.sparkline7d ?? []).map((p, i) => ({ i, p }));
              return (
                <Link
                  key={c.symbol}
                  to="/asset/$symbol"
                  params={{ symbol: c.symbol }}
                  className="group rounded-xl border border-border bg-card p-5 transition hover:border-primary/40 hover:shadow-lg"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      {c.image && (
                        <img src={c.image} alt={c.name} className="h-9 w-9 rounded-full" />
                      )}
                      <div>
                        <p className="text-xs text-muted-foreground">{c.name}</p>
                        <p className="text-lg font-semibold">{c.symbol}</p>
                      </div>
                    </div>
                    <span
                      className={`flex items-center gap-1 text-xs font-medium ${
                        up ? "text-primary" : "text-destructive"
                      }`}
                    >
                      {up ? <TrendingUp className="h-3.5 w-3.5" /> : <TrendingDown className="h-3.5 w-3.5" />}
                      {c.change24h > 0 ? "+" : ""}
                      {c.change24h.toFixed(2)}%
                    </span>
                  </div>

                  <p className="mt-4 text-2xl font-bold tabular-nums">{formatNGN(c.rate)}</p>

                  {spark.length > 1 && (
                    <div className="mt-3 h-12 -mx-1">
                      <ResponsiveContainer width="100%" height="100%">
                        <AreaChart data={spark} margin={{ top: 2, right: 2, left: 2, bottom: 2 }}>
                          <defs>
                            <linearGradient id={`sp-${c.symbol}`} x1="0" y1="0" x2="0" y2="1">
                              <stop
                                offset="0%"
                                stopColor={up ? "oklch(0.78 0.18 150)" : "oklch(0.65 0.2 25)"}
                                stopOpacity={0.5}
                              />
                              <stop
                                offset="100%"
                                stopColor={up ? "oklch(0.78 0.18 150)" : "oklch(0.65 0.2 25)"}
                                stopOpacity={0}
                              />
                            </linearGradient>
                          </defs>
                          <Area
                            type="monotone"
                            dataKey="p"
                            stroke={up ? "oklch(0.78 0.18 150)" : "oklch(0.65 0.2 25)"}
                            strokeWidth={1.5}
                            fill={`url(#sp-${c.symbol})`}
                            isAnimationActive={false}
                          />
                        </AreaChart>
                      </ResponsiveContainer>
                    </div>
                  )}

                  <div className="mt-3 grid grid-cols-2 gap-2 text-xs text-muted-foreground">
                    <div>
                      <p className="text-[10px] uppercase tracking-wider">Mkt cap</p>
                      <p className="text-foreground">{c.marketCap ? formatCompactNGN(c.marketCap) : "—"}</p>
                    </div>
                    <div>
                      <p className="text-[10px] uppercase tracking-wider">24h vol</p>
                      <p className="text-foreground">{c.volume24h ? formatCompactNGN(c.volume24h) : "—"}</p>
                    </div>
                  </div>
                </Link>
              );
            })}
          </div>
        </section>

        <section>
          <h2 className="mb-3 text-sm font-medium uppercase tracking-wider text-muted-foreground">
            Recent transactions
          </h2>
          <TransactionTable txs={txs} />
        </section>
      </main>
    </div>
  );
}
