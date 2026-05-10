import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { useEffect, useMemo, useState } from "react";
import { Copy } from "lucide-react";
import { toast } from "sonner";
import { Header } from "@/components/Header";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAuth } from "@/context/AuthContext";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import { createSellOrder, getAdminWallet, getRates } from "@/services/api";
import type { Crypto } from "@/services/mockData";
import { formatCrypto, formatNGN } from "@/utils/format";

export const Route = createFileRoute("/sell")({
  head: () => ({ meta: [{ title: "Sell crypto — Brokr" }] }),
  component: SellPage,
});

function SellPage() {
  const { ready } = useRequireAuth();
  const { user } = useAuth();
  const navigate = useNavigate();
  const [rates, setRates] = useState<Crypto[]>([]);
  const [symbol, setSymbol] = useState("BTC");
  const [cryptoAmount, setCryptoAmount] = useState<number>(0.001);
  const [confirmed, setConfirmed] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    getRates().then(setRates);
  }, []);

  const selected = useMemo(() => rates.find((r) => r.symbol === symbol), [rates, symbol]);
  const fiatAmount = selected ? Math.round(cryptoAmount * selected.rate) : 0;
  const adminWallet = getAdminWallet(symbol);

  const copy = () => {
    navigator.clipboard.writeText(adminWallet);
    toast.success("Address copied");
  };

  const submit = async () => {
    if (!user || !selected) return;
    if (cryptoAmount <= 0) {
      toast.error("Enter a valid amount");
      return;
    }
    if (!confirmed) {
      toast.error("Please confirm you've sent the crypto");
      return;
    }
    setSubmitting(true);
    try {
      await createSellOrder({
        userId: user.id,
        userEmail: user.email,
        crypto: symbol,
        fiatAmount,
        cryptoAmount,
        walletAddress: adminWallet,
      });
      toast.success("Sell order submitted. Awaiting admin confirmation.");
      navigate({ to: "/dashboard" });
    } catch (e) {
      toast.error(e instanceof Error ? e.message : "Order failed");
    } finally {
      setSubmitting(false);
    }
  };

  if (!ready) return null;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main className="mx-auto max-w-xl px-4 py-10">
        <h1 className="text-3xl font-bold tracking-tight">Sell crypto</h1>
        <p className="mt-2 text-sm text-muted-foreground">
          Send crypto to our wallet. We send naira after confirmation.
        </p>

        <div className="mt-8 rounded-xl border border-border bg-card p-6 space-y-5">
          <div className="space-y-2">
            <Label>Asset</Label>
            <div className="grid grid-cols-3 gap-2">
              {rates.map((r) => (
                <button
                  key={r.symbol}
                  type="button"
                  onClick={() => setSymbol(r.symbol)}
                  className={`rounded-lg border px-3 py-2 text-sm font-medium transition ${
                    symbol === r.symbol
                      ? "border-primary bg-primary/10 text-foreground"
                      : "border-border text-muted-foreground hover:text-foreground"
                  }`}
                >
                  {r.symbol}
                </button>
              ))}
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="amt">You send</Label>
            <Input
              id="amt"
              type="number"
              step="0.0001"
              min={0}
              value={cryptoAmount}
              onChange={(e) => setCryptoAmount(Number(e.target.value))}
            />
            <p className="text-xs text-muted-foreground">
              {selected ? formatCrypto(cryptoAmount, selected.symbol) : ""}
            </p>
          </div>

          <div className="rounded-lg bg-muted/50 px-4 py-3 text-sm">
            You receive ≈{" "}
            <span className="font-semibold text-foreground">{formatNGN(fiatAmount)}</span>
          </div>

          <div className="space-y-2">
            <Label>Send {symbol} to this address</Label>
            <div className="flex gap-2">
              <Input readOnly value={adminWallet} className="font-mono text-xs" />
              <Button variant="outline" size="icon" onClick={copy} aria-label="Copy">
                <Copy className="h-4 w-4" />
              </Button>
            </div>
          </div>

          <label className="flex items-start gap-2 text-sm text-muted-foreground">
            <input
              type="checkbox"
              className="mt-1"
              checked={confirmed}
              onChange={(e) => setConfirmed(e.target.checked)}
            />
            I have sent {selected ? formatCrypto(cryptoAmount, selected.symbol) : "the crypto"}{" "}
            to the address above.
          </label>

          <Button onClick={submit} disabled={submitting} className="w-full">
            {submitting ? "Submitting…" : "Submit sell order"}
          </Button>
        </div>
      </main>
    </div>
  );
}
