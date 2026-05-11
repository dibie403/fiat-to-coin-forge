import { createFileRoute, useNavigate } from "@tanstack/react-router";
import { useEffect, useMemo, useState } from "react";
import { toast } from "sonner";
import { Header } from "@/components/Header";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAuth } from "@/context/AuthContext";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import { createBuyOrder, getRates, updateTransactionStatus } from "@/services/api";
import { initializePayment, verifyPayment } from "@/services/paystack";
import type { Crypto } from "@/services/mockData";
import { formatCrypto, formatNGN } from "@/utils/format";

export const Route = createFileRoute("/buy")({
  head: () => ({ meta: [{ title: "Buy crypto — Orji Funds Exchange" }] }),
  component: BuyPage,
});

function BuyPage() {
  const { ready } = useRequireAuth();
  const { user } = useAuth();
  const navigate = useNavigate();
  const [rates, setRates] = useState<Crypto[]>([]);
  const [symbol, setSymbol] = useState("BTC");
  const [fiatAmount, setFiatAmount] = useState<number>(50000);
  const [wallet, setWallet] = useState("");
  const [step, setStep] = useState<"form" | "paying" | "verifying" | "done">("form");
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    getRates().then(setRates);
  }, []);

  const selected = useMemo(() => rates.find((r) => r.symbol === symbol), [rates, symbol]);
  const cryptoAmount = selected && fiatAmount > 0 ? fiatAmount / selected.rate : 0;

  const submit = async () => {
    if (!user || !selected) return;
    if (!wallet.trim() || wallet.length < 10) {
      toast.error("Please enter a valid wallet address");
      return;
    }
    if (fiatAmount < 1000) {
      toast.error("Minimum buy amount is ₦1,000");
      return;
    }
    setSubmitting(true);
    try {
      const tx = await createBuyOrder({
        userId: user.id,
        userEmail: user.email,
        crypto: symbol,
        fiatAmount,
        cryptoAmount,
        walletAddress: wallet.trim(),
      });
      setStep("paying");
      const init = await initializePayment({
        email: user.email,
        amount: fiatAmount,
        metadata: { txId: tx.id },
      });
      toast.info("Paystack: payment initialized");
      setStep("verifying");
      const v = await verifyPayment(init.reference);
      if (v.status === "success") {
        await updateTransactionStatus(tx.id, "PAID");
        toast.success("Payment confirmed. Pending crypto delivery.");
      } else {
        await updateTransactionStatus(tx.id, "FAILED");
        toast.error("Payment failed");
      }
      setStep("done");
      setTimeout(() => navigate({ to: "/dashboard" }), 1200);
    } catch (e) {
      toast.error(e instanceof Error ? e.message : "Order failed");
      setStep("form");
    } finally {
      setSubmitting(false);
    }
  };

  if (!ready) return null;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main className="mx-auto max-w-xl px-4 py-10">
        <h1 className="text-3xl font-bold tracking-tight">Buy crypto</h1>
        <p className="mt-2 text-sm text-muted-foreground">
          Pay with naira via Paystack. Crypto sent to your wallet after confirmation.
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
            {selected && (
              <p className="text-xs text-muted-foreground">
                1 {selected.symbol} ≈ {formatNGN(selected.rate)}
              </p>
            )}
          </div>

          <div className="space-y-2">
            <Label htmlFor="fiat">You pay (NGN)</Label>
            <Input
              id="fiat"
              type="number"
              min={1000}
              value={fiatAmount}
              onChange={(e) => setFiatAmount(Number(e.target.value))}
            />
          </div>

          <div className="rounded-lg bg-muted/50 px-4 py-3 text-sm">
            You receive ≈{" "}
            <span className="font-semibold text-foreground">
              {selected ? formatCrypto(cryptoAmount, selected.symbol) : "—"}
            </span>
          </div>

          <div className="space-y-2">
            <Label htmlFor="wallet">Your {symbol} wallet address</Label>
            <Input
              id="wallet"
              value={wallet}
              onChange={(e) => setWallet(e.target.value)}
              placeholder={`Paste your ${symbol} address`}
            />
          </div>

          <Button onClick={submit} disabled={submitting} className="w-full">
            {step === "form" && (submitting ? "Creating order…" : "Continue to payment")}
            {step === "paying" && "Opening Paystack…"}
            {step === "verifying" && "Verifying payment…"}
            {step === "done" && "Done — redirecting"}
          </Button>
        </div>
      </main>
    </div>
  );
}
