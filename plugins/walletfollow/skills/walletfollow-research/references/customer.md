# Portfolio and own-account read semantics

Read [customer-read-schema.json](customer-read-schema.json) for accepted arguments and [the operation index](api-operations.md) for tool names. Resource IDs, creator handles, slugs and immutable version numbers come from the API. Public copy and market reads require the customer's research access; private reports require the exact OAuth read scope plus a current corresponding customer API grant and permitted account ownership. Private account/trading access retains a separate pilot restriction even after verified-user research opens. An OAuth connection cannot broaden that restriction.

## Public market and copy research

`wf_get_trade_markets_summary` and market `positioning`, `tape`, `history` reads describe prepared market observations. Preserve market identity, timestamps and coverage. These are different from the bounded candle source.

Public copy tools expose capabilities, engine scope, catalog/shelves, creator profiles, portfolio details, immutable versions, copyability, stats, exposure, feed and cards. Start from the portfolio catalog, then request the relevant exact `handle`/`slug`. A catalog's `tab:"watched"` is customer-specific and additionally needs `copy:read`. Keep leader weights and fee schedules tied to their returned version. A published definition, an engine eligibility result, a profitable historical period and an effective active copy are different states.

Statistics may be partial, stale, missing, modeled or unavailable. Describe the returned metric's basis and period. Incomplete ideal proportional copy ROI must remain incomplete/null; account PnL is not a substitute. Do not rank or promise real-world returns from a missing starting state, unknown capital flows, retained partial history or paper/fake execution results.

## Private reads

| OAuth/read-grant scope | Customer reports |
| --- | --- |
| `wallets:read` | Own bookmarked wallets and limit. A bookmark does not prove wallet ownership. |
| `trading-accounts:read` | Own permitted linked accounts, details and setup prechecks. A precheck does not grant an approval or submit a signature. |
| `trade:read` | Own watched positions and manual intent/status list. An intent/status is not independently verified exchange execution. |
| `copy:read` | Compatibility catalog, capabilities, subscriptions, setup prechecks, desired/effective status, bounded results/fills/orders/decisions, watches and invoices. |
| `creator:read` | Own creator profile/workspaces, leader returns, earnings, statements and recorded payout identity. Records do not prove funds were paid out. |

Finite account restrictions filter collections and referenced subscription/order IDs. A denial or omitted account cannot be circumvented with an arbitrary ID. Aggregate invoices can require unrestricted own-account access. Public information about a wallet does not authorize its private reports.

For status questions, report desired state and effective engine state separately with their timestamps and refusal reasons. An engine-off response or unsupported capability is not success. When existing reports contain `REQUESTED`/HTTP 202 semantics, describe durable command creation only; do not infer a fill, activation or closure. Account and creator fee ledgers are informational; this plugin does not pay invoices, deduct funds or execute payouts.

## Full API controls are outside this plugin

[customer-control-schema.json](customer-control-schema.json) documents the existing 38 non-GET operations and exact validated input shape for developers. Read it only when explaining a specific dashboard/API control. These tools are absent from the marketplace MCP; do not issue direct HTTP requests to bypass that profile.

The API controls cover bookmark changes; SIWE challenge/proof and account hints/disconnect; manual place/modify/cancel intents; copy drafts, versions, risk/consent updates, submission/discard/setup/start/pause/resume/stop/close/revoke/excluded markets; portfolio watches/reports; creator profiles, drafts, previews, publication/visibility/archive/fees/affiliation; bounded leader checks; and verification-only payout identity. Browser-only credential/permission management is not part of bearer API routing.

These controls retain ownership, explicit consent, account restrictions, recent-auth, capability, engine and idempotency checks. A caller normally needs matching read and write permissions; write grants expire no later than 24 hours and read-only grants no later than 30 days. Mutations require a stable `Idempotency-Key` for the exact operation and preserve body/identity on retries. A transport uncertainty is not permission to duplicate an order with a new identity. Do not create API grants from the plugin.

Route control requests to [the customer's WalletFollow dashboard](https://walletfollow.ai/account) and explain the requested action's effect accurately. Never request a private key, API-wallet key, seed, customer signature, signed venue action or invoice payment. The customer follows any explicitly enabled wallet signing flow in the dashboard. The marketplace plugin itself requests no wallet signature and submits no Hyperliquid `/exchange` request.
