import type { Transaction } from "@/services/mockData";
import { Badge } from "@/components/ui/badge";
import { formatCrypto, formatDate, formatNGN } from "@/utils/format";

const statusVariant: Record<Transaction["status"], string> = {
  PENDING_PAYMENT: "bg-amber-500/15 text-amber-600 dark:text-amber-400 border-amber-500/30",
  PAID: "bg-blue-500/15 text-blue-600 dark:text-blue-400 border-blue-500/30",
  PENDING_ADMIN_CONFIRMATION:
    "bg-purple-500/15 text-purple-600 dark:text-purple-400 border-purple-500/30",
  COMPLETED: "bg-primary/15 text-primary border-primary/30",
  FAILED: "bg-destructive/15 text-destructive border-destructive/30",
};

export function TxStatusBadge({ status }: { status: Transaction["status"] }) {
  return (
    <Badge variant="outline" className={statusVariant[status]}>
      {status.replace(/_/g, " ")}
    </Badge>
  );
}

export function TransactionTable({ txs }: { txs: Transaction[] }) {
  if (txs.length === 0) {
    return (
      <div className="rounded-lg border border-dashed border-border p-8 text-center text-sm text-muted-foreground">
        No transactions yet.
      </div>
    );
  }
  return (
    <div className="overflow-x-auto rounded-lg border border-border">
      <table className="w-full text-sm">
        <thead className="bg-muted/50 text-left text-xs uppercase text-muted-foreground">
          <tr>
            <th className="px-4 py-3 font-medium">Date</th>
            <th className="px-4 py-3 font-medium">Type</th>
            <th className="px-4 py-3 font-medium">Asset</th>
            <th className="px-4 py-3 font-medium">Crypto</th>
            <th className="px-4 py-3 font-medium">Fiat</th>
            <th className="px-4 py-3 font-medium">Status</th>
          </tr>
        </thead>
        <tbody>
          {txs.map((t) => (
            <tr key={t.id} className="border-t border-border">
              <td className="px-4 py-3 whitespace-nowrap text-muted-foreground">
                {formatDate(t.timestamp)}
              </td>
              <td className="px-4 py-3 font-medium">{t.type}</td>
              <td className="px-4 py-3">{t.crypto}</td>
              <td className="px-4 py-3">{formatCrypto(t.cryptoAmount, t.crypto)}</td>
              <td className="px-4 py-3">{formatNGN(t.fiatAmount)}</td>
              <td className="px-4 py-3"><TxStatusBadge status={t.status} /></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
