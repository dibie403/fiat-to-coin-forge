# Brokr — Crypto Brokerage Platform

A modern, semi-manual crypto brokerage built with **TanStack Start (React + Vite)** and **Tailwind CSS**. Users buy and sell BTC / ETH / USDT with naira; admins manually approve transactions.

> **Status:** Frontend with a fully mocked API layer. Designed to swap to a Django REST backend with zero component changes.

---

## 1. System overview

```
┌────────────────────────────┐      ┌──────────────────────────┐
│  React Frontend (this app) │ ───▶ │  /services/api.ts (mock) │
│  - Pages, Auth, Admin      │      │   localStorage-backed    │
└────────────────────────────┘      └──────────────────────────┘
                                              │
                                              ▼  (swap later)
                                    ┌──────────────────────┐
                                    │  Django REST API     │
                                    │  + Paystack          │
                                    └──────────────────────┘
```

### Flows

- **Buy:** select crypto → enter NGN → enter wallet → mock Paystack pay → `PENDING_PAYMENT` → `PAID` → admin marks `COMPLETED`.
- **Sell:** select crypto → enter amount → see admin wallet → confirm sent → `PENDING_ADMIN_CONFIRMATION` → admin marks `COMPLETED`.
- **Admin:** approves/rejects orders, edits rates, views users.

### Demo credentials

| Role  | Email             | Password   |
|-------|-------------------|------------|
| User  | `demo@brokr.io`   | `demo123`  |
| Admin | `admin@brokr.io`  | `admin123` |

---

## 2. Project structure

```
src/
  components/        # Header, TransactionTable, TxStatusBadge, ui/
  context/           # AuthContext.tsx
  hooks/             # useRequireAuth.ts
  routes/            # index, login, register, dashboard, buy, sell, admin
  services/
    api.ts           # mock API — single point of integration
    mockData.ts      # types + seed data
    paystack.ts      # mock Paystack init/verify
  utils/             # format helpers
```

To swap to Django: replace the function bodies in `src/services/api.ts` and `src/services/paystack.ts` with `fetch`/`axios` calls. **Components import only from `@/services/*` — no business logic lives in pages.**

---

## 3. API endpoints (target Django backend)

### Auth
```
POST  /api/auth/register   { name, email, password }   → { token, user }
POST  /api/auth/login      { email, password }         → { token, user }
GET   /api/auth/user       (Bearer)                    → { user }
```

### Rates
```
GET   /api/rates                                       → [{ symbol, name, rate, change24h }]
PUT   /api/rates/update    { symbol, rate }   (admin)  → updated rate
```

### Transactions
```
POST  /api/transactions/buy
      { crypto, fiatAmount, cryptoAmount, walletAddress }
      → Transaction (status=PENDING_PAYMENT)

POST  /api/transactions/sell
      { crypto, fiatAmount, cryptoAmount, walletAddress }
      → Transaction (status=PENDING_ADMIN_CONFIRMATION)

GET   /api/transactions/user/:id                       → Transaction[]
GET   /api/transactions/admin            (admin)       → Transaction[]
PATCH /api/transactions/update-status    (admin)
      { id, status }                                   → Transaction
```

### Paystack (server-side proxy recommended)
```
POST  /api/payments/initialize   { email, amount, metadata }
POST  /api/payments/verify       { reference }
POST  /api/payments/webhook      (Paystack → server, signature verified)
```

---

## 4. Data models

### User
```json
{
  "id": "string",
  "name": "string",
  "email": "string",
  "password": "string (hashed server-side)",
  "role": "user | admin"
}
```

### Transaction
```json
{
  "id": "string",
  "userId": "string",
  "userEmail": "string",
  "type": "BUY | SELL",
  "crypto": "BTC | ETH | USDT",
  "fiatAmount": 0,
  "cryptoAmount": 0,
  "walletAddress": "string",
  "status": "PENDING_PAYMENT | PAID | PENDING_ADMIN_CONFIRMATION | COMPLETED | FAILED",
  "timestamp": "ISO-8601"
}
```

### Rate
```json
{ "symbol": "BTC", "name": "Bitcoin", "rate": 65000000, "change24h": 2.34 }
```

---

## 5. Transaction states

```
BUY:  PENDING_PAYMENT → PAID → COMPLETED
                              ↘ FAILED
SELL: PENDING_ADMIN_CONFIRMATION → COMPLETED
                                 ↘ FAILED
```

---

## 6. Integration checklist

- [ ] Replace functions in `src/services/api.ts` with HTTP calls.
- [ ] Replace `src/services/paystack.ts` with calls to your backend payment proxy.
- [ ] Move JWT to httpOnly cookie or `Authorization: Bearer` header (currently stored in `localStorage` for the mock).
- [ ] Implement Paystack webhook on Django to flip `PENDING_PAYMENT` → `PAID`.
- [ ] Add server-side validation (Django + DRF serializers).
- [ ] Enforce role checks server-side for `/admin` endpoints.
