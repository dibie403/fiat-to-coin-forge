import { Link } from "@tanstack/react-router";
import { Logo } from "@/components/Logo";

export function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer className="border-t border-border/60 bg-card/40 mt-16">
      <div className="mx-auto max-w-6xl px-4 py-12 grid gap-8 md:grid-cols-4">
        <div className="md:col-span-2">
          <Logo size="md" asLink={false} />
          <p className="mt-4 max-w-sm text-sm text-muted-foreground">
            Buy and sell Bitcoin, Ethereum and USDT with naira. Transparent
            rates, real humans, lightning-fast settlements.
          </p>
        </div>

        <div>
          <h4 className="text-sm font-semibold">Product</h4>
          <ul className="mt-3 space-y-2 text-sm text-muted-foreground">
            <li><Link to="/buy" className="hover:text-foreground">Buy crypto</Link></li>
            <li><Link to="/sell" className="hover:text-foreground">Sell crypto</Link></li>
            <li><Link to="/dashboard" className="hover:text-foreground">Dashboard</Link></li>
          </ul>
        </div>

        <div>
          <h4 className="text-sm font-semibold">Account</h4>
          <ul className="mt-3 space-y-2 text-sm text-muted-foreground">
            <li><Link to="/login" className="hover:text-foreground">Sign in</Link></li>
            <li><Link to="/register" className="hover:text-foreground">Create account</Link></li>
          </ul>
        </div>
      </div>
      <div className="border-t border-border/60">
        <div className="mx-auto max-w-6xl px-4 py-5 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-muted-foreground">
          <p>© {year} Orji Funds Exchange. All rights reserved.</p>
          <p>Trade responsibly. Crypto prices can be volatile.</p>
        </div>
      </div>
    </footer>
  );
}
