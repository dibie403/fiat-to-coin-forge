import { createFileRoute, Link } from "@tanstack/react-router";
import { ArrowRight, ShieldCheck, Zap, Wallet } from "lucide-react";
import { Header } from "@/components/Header";
import { Button } from "@/components/ui/button";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "Brokr — Buy & sell crypto with naira" },
      {
        name: "description",
        content:
          "Brokr is a fast, simple crypto brokerage. Buy and sell BTC, ETH, and USDT with naira in minutes.",
      },
      { property: "og:title", content: "Brokr — Buy & sell crypto with naira" },
      {
        property: "og:description",
        content: "Buy and sell BTC, ETH, and USDT with naira in minutes.",
      },
    ],
  }),
  component: Home,
});

function Home() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main>
        <section className="mx-auto max-w-6xl px-4 pt-20 pb-24 text-center">
          <div className="inline-flex items-center gap-2 rounded-full border border-border bg-card px-3 py-1 text-xs text-muted-foreground">
            <span className="h-2 w-2 rounded-full bg-primary animate-pulse" />
            Live rates · Naira settlements
          </div>
          <h1 className="mt-6 text-5xl md:text-6xl font-bold tracking-tight">
            Crypto, the way it should{" "}
            <span className="bg-gradient-to-r from-primary to-emerald-400 bg-clip-text text-transparent">
              feel.
            </span>
          </h1>
          <p className="mt-5 mx-auto max-w-xl text-lg text-muted-foreground">
            Buy and sell Bitcoin, Ethereum and USDT with naira. Transparent
            rates, real humans, lightning-fast settlements.
          </p>
          <div className="mt-8 flex justify-center gap-3">
            <Link to="/register">
              <Button size="lg" className="gap-2">
                Create account <ArrowRight className="h-4 w-4" />
              </Button>
            </Link>
            <Link to="/login">
              <Button size="lg" variant="outline">
                Sign in
              </Button>
            </Link>
          </div>
          <p className="mt-3 text-xs text-muted-foreground">
            Demo: <code className="text-foreground">demo@brokr.io</code> /{" "}
            <code className="text-foreground">demo123</code> · Admin:{" "}
            <code className="text-foreground">admin@brokr.io</code> /{" "}
            <code className="text-foreground">admin123</code>
          </p>
        </section>

        <section className="mx-auto max-w-6xl px-4 pb-24 grid md:grid-cols-3 gap-4">
          {[
            {
              icon: Zap,
              title: "Instant quotes",
              body: "Live mid-market rates refreshed every few seconds.",
            },
            {
              icon: ShieldCheck,
              title: "Human-reviewed",
              body: "Every order is double-checked before settlement.",
            },
            {
              icon: Wallet,
              title: "Naira native",
              body: "Pay with Paystack, settle straight to your wallet.",
            },
          ].map(({ icon: Icon, title, body }) => (
            <div
              key={title}
              className="rounded-xl border border-border bg-card p-6 transition hover:border-primary/40"
            >
              <Icon className="h-6 w-6 text-primary" />
              <h3 className="mt-4 font-semibold">{title}</h3>
              <p className="mt-1 text-sm text-muted-foreground">{body}</p>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
}
