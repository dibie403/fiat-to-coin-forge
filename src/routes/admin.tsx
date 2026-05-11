import { createFileRoute } from "@tanstack/react-router";
import { useEffect, useState } from "react";
import { toast } from "sonner";
import { Header } from "@/components/Header";
import { TxStatusBadge } from "@/components/TransactionTable";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import {
  getAdminOrders,
  getStoredRates,
  listUsers,
  updateRate,
  updateTransactionStatus,
} from "@/services/api";
import type { Crypto, Transaction, User } from "@/services/mockData";
import { formatCrypto, formatDate, formatNGN } from "@/utils/format";

export const Route = createFileRoute("/admin")({
  head: () => ({ meta: [{ title: "Admin — Orji Funds Exchange" }] }),
  component: AdminPage,
});

type Tab = "buys" | "sells" | "rates" | "users";

function AdminPage() {
  const { ready } = useRequireAuth({ adminOnly: true });
  const [tab, setTab] = useState<Tab>("buys");
  const [orders, setOrders] = useState<Transaction[]>([]);
  const [rates, setRates] = useState<Crypto[]>([]);
  const [users, setUsers] = useState<Omit<User, "password">[]>([]);

  const refresh = async () => {
    const [o, u] = await Promise.all([getAdminOrders(), listUsers()]);
    setOrders(o);
    setUsers(u);
    setRates(getStoredRates());
  };

  useEffect(() => {
    if (ready) refresh();
  }, [ready]);

  if (!ready) return null;

  const buys = orders.filter((o) => o.type === "BUY");
  const sells = orders.filter((o) => o.type === "SELL");

  const setStatus = async (id: string, status: Transaction["status"]) => {
    await updateTransactionStatus(id, status);
    toast.success("Order updated");
    refresh();
  };

  const saveRate = async (symbol: string, rate: number) => {
    await updateRate(symbol, rate);
    toast.success(`${symbol} rate updated`);
    refresh();
  };

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main className="mx-auto max-w-6xl px-4 py-10">
        <h1 className="text-3xl font-bold tracking-tight">Admin console</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Approve orders, manage rates, view users.
        </p>

        <div className="mt-6 inline-flex rounded-lg border border-border bg-card p-1">
          {([
            ["buys", `Buy orders (${buys.length})`],
            ["sells", `Sell orders (${sells.length})`],
            ["rates", "Rates"],
            ["users", `Users (${users.length})`],
          ] as [Tab, string][]).map(([k, label]) => (
            <button
              key={k}
              onClick={() => setTab(k)}
              className={`rounded-md px-3 py-1.5 text-sm font-medium transition ${
                tab === k ? "bg-primary text-primary-foreground" : "text-muted-foreground hover:text-foreground"
              }`}
            >
              {label}
            </button>
          ))}
        </div>

        <div className="mt-6">
          {tab === "buys" && (
            <OrderList
              orders={buys}
              renderActions={(o) =>
                o.status === "PAID" ? (
                  <>
                    <Button size="sm" onClick={() => setStatus(o.id, "COMPLETED")}>
                      Mark crypto sent
                    </Button>
                    <Button size="sm" variant="outline" onClick={() => setStatus(o.id, "FAILED")}>
                      Reject
                    </Button>
                  </>
                ) : null
              }
            />
          )}
          {tab === "sells" && (
            <OrderList
              orders={sells}
              renderActions={(o) =>
                o.status === "PENDING_ADMIN_CONFIRMATION" ? (
                  <>
                    <Button size="sm" onClick={() => setStatus(o.id, "COMPLETED")}>
                      Approve & pay fiat
                    </Button>
                    <Button size="sm" variant="outline" onClick={() => setStatus(o.id, "FAILED")}>
                      Reject
                    </Button>
                  </>
                ) : null
              }
            />
          )}
          {tab === "rates" && <RatesEditor rates={rates} onSave={saveRate} />}
          {tab === "users" && <UsersList users={users} />}
        </div>
      </main>
    </div>
  );
}

function OrderList({
  orders,
  renderActions,
}: {
  orders: Transaction[];
  renderActions: (o: Transaction) => React.ReactNode;
}) {
  if (orders.length === 0) {
    return (
      <div className="rounded-lg border border-dashed border-border p-8 text-center text-sm text-muted-foreground">
        No orders.
      </div>
    );
  }
  return (
    <div className="space-y-3">
      {orders.map((o) => (
        <div
          key={o.id}
          className="rounded-xl border border-border bg-card p-5 flex flex-wrap items-center justify-between gap-4"
        >
          <div className="space-y-1 text-sm">
            <div className="flex items-center gap-2">
              <span className="font-semibold">{o.type}</span>
              <span className="text-muted-foreground">·</span>
              <span>{o.crypto}</span>
              <TxStatusBadge status={o.status} />
            </div>
            <div className="text-muted-foreground">
              {formatCrypto(o.cryptoAmount, o.crypto)} ↔ {formatNGN(o.fiatAmount)}
            </div>
            <div className="text-xs text-muted-foreground">
              {o.userEmail} · {formatDate(o.timestamp)}
            </div>
            <div className="text-xs font-mono break-all text-muted-foreground">
              {o.walletAddress}
            </div>
          </div>
          <div className="flex gap-2">{renderActions(o)}</div>
        </div>
      ))}
    </div>
  );
}

function RatesEditor({
  rates,
  onSave,
}: {
  rates: Crypto[];
  onSave: (symbol: string, rate: number) => void;
}) {
  const [draft, setDraft] = useState<Record<string, number>>(
    Object.fromEntries(rates.map((r) => [r.symbol, r.rate])),
  );
  useEffect(() => {
    setDraft(Object.fromEntries(rates.map((r) => [r.symbol, r.rate])));
  }, [rates]);
  return (
    <div className="space-y-3">
      {rates.map((r) => (
        <div
          key={r.symbol}
          className="flex flex-wrap items-center gap-3 rounded-xl border border-border bg-card p-4"
        >
          <div className="w-32">
            <p className="font-semibold">{r.symbol}</p>
            <p className="text-xs text-muted-foreground">{r.name}</p>
          </div>
          <Input
            type="number"
            value={draft[r.symbol]}
            onChange={(e) => setDraft({ ...draft, [r.symbol]: Number(e.target.value) })}
            className="max-w-xs"
          />
          <Button size="sm" onClick={() => onSave(r.symbol, draft[r.symbol])}>
            Save
          </Button>
        </div>
      ))}
    </div>
  );
}

function UsersList({ users }: { users: Omit<User, "password">[] }) {
  return (
    <div className="overflow-x-auto rounded-lg border border-border">
      <table className="w-full text-sm">
        <thead className="bg-muted/50 text-left text-xs uppercase text-muted-foreground">
          <tr>
            <th className="px-4 py-3 font-medium">Name</th>
            <th className="px-4 py-3 font-medium">Email</th>
            <th className="px-4 py-3 font-medium">Role</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.id} className="border-t border-border">
              <td className="px-4 py-3">{u.name}</td>
              <td className="px-4 py-3 text-muted-foreground">{u.email}</td>
              <td className="px-4 py-3 capitalize">{u.role}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
