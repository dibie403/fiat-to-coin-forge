import { createFileRoute, Link } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { ArrowDownRight, ArrowUpRight, TrendingUp, TrendingDown } from "lucide-react";
import { Header } from "@/components/Header";
import { TransactionTable } from "@/components/TransactionTable";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/context/AuthContext";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import { getRates, getUserTransactions } from "@/services/api";
import type { Crypto, Transaction } from "@/services/mockData";
import { formatNGN } from "@/utils/format";

export const Route = createFileRoute("/dashboard")({
  head: () => ({ meta: [{ title: "Dashboard — Brokr" }] }),
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
    const id = setInterval(() => getRates().then((r) => live && setRates(r)), 5000);
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
              return (
                <div
                  key={c.symbol}
                  className="rounded-xl border border-border bg-card p-5 transition hover:border-primary/40"
                >
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-xs text-muted-foreground">{c.name}</p>
                      <p className="text-lg font-semibold">{c.symbol}</p>
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
                  <p className="mt-4 text-2xl font-bold tabular-nums">
                    {formatNGN(c.rate)}
                  </p>
                </div>
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
