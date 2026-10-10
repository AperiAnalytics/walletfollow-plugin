# Complete API operation index

Generated from the canonical MCP tool catalog and API registries. 100 HTTP operations are represented. Source implementation does not guarantee customer access or deployed availability. Backend pilot, permissions, plan and engine gates remain authoritative.

The marketplace exposes GET reads only. Every non-GET row is documented for API understanding and unavailable through this plugin. Route those requests to the customer dashboard without a direct-HTTP workaround. Scopes in this table are MCP OAuth scopes; public research maps to the API key’s `api:data` entitlement. Private account reads also require the existing matching live customer grant and permitted account ownership.

Path arguments are top-level named tool arguments. API query values belong inside `query`. Each schema reference contains the exact input schema and endpoint: read only the reference relevant to the request.

## Public wallet research and metadata

Detailed input schemas: [research-schema.json](research-schema.json).

| Tool | HTTP operation | OAuth scope | Marketplace |
| --- | --- | --- | --- |
| `wf_get_wallet` | `GET /v1/wallets/{address}` | `data:read` | Read |
| `wf_get_wallet_account` | `GET /v1/wallets/{address}/account` | `data:read` | Read |
| `wf_get_wallet_positions` | `GET /v1/wallets/{address}/positions` | `data:read` | Read |
| `wf_get_wallet_spot` | `GET /v1/wallets/{address}/spot` | `data:read` | Read |
| `wf_get_wallet_metrics` | `GET /v1/wallets/{address}/metrics` | `data:read` | Read |
| `wf_get_wallet_profile` | `GET /v1/wallets/{address}/profile` | `data:read` | Read |
| `wf_get_wallet_analysis` | `GET /v1/wallets/{address}/analysis` | `data:read` | Read |
| `wf_get_wallet_trades` | `GET /v1/wallets/{address}/trades` | `data:read` | Read |
| `wf_get_wallet_screener` | `GET /v1/wallets/top` | `data:read` | Read |
| `wf_get_wallet_open_orders` | `GET /v1/wallets/{address}/open-orders` | `data:read` | Read |
| `wf_get_wallet_order_history` | `GET /v1/wallets/{address}/order-history` | `data:read` | Read |
| `wf_get_wallet_fills` | `GET /v1/wallets/{address}/fills` | `data:read` | Read |
| `wf_get_wallet_funding` | `GET /v1/wallets/{address}/funding` | `data:read` | Read |
| `wf_get_wallet_transfers` | `GET /v1/wallets/{address}/transfers` | `data:read` | Read |
| `wf_get_wallet_vaults` | `GET /v1/wallets/{address}/vaults` | `data:read` | Read |
| `wf_get_wallet_staking` | `GET /v1/wallets/{address}/staking` | `data:read` | Read |
| `wf_get_wallet_portfolio` | `GET /v1/wallets/{address}/portfolio` | `data:read` | Read |
| `wf_get_markets_coin_candles` | `GET /v1/markets/{coin}/candles` | `data:read` | Read |
| `wf_get_usage` | `GET /v1/usage` | `data:read` | Read |
| `wf_get_catalog` | `GET /v1/catalog` | `data:read` | Read |
| `wf_get_openapi_json` | `GET /v1/openapi.json` | `data:read` | Read |

## Portfolio, market and permitted account reads

Detailed input schemas: [customer-read-schema.json](customer-read-schema.json).

| Tool | HTTP operation | OAuth scope | Marketplace |
| --- | --- | --- | --- |
| `wf_get_account_wallets` | `GET /v1/account/wallets` | `wallets:read` | Read |
| `wf_get_account_trading_accounts` | `GET /v1/account/trading-accounts` | `trading-accounts:read` | Read |
| `wf_get_account_trading_accounts_id` | `GET /v1/account/trading-accounts/{id}` | `trading-accounts:read` | Read |
| `wf_get_account_trading_accounts_id_setup_precheck` | `GET /v1/account/trading-accounts/{id}/setup-precheck` | `trading-accounts:read` | Read |
| `wf_get_trade_markets_summary` | `GET /v1/trade/markets/summary` | `data:read` | Read |
| `wf_get_trade_markets_coin_positioning` | `GET /v1/trade/markets/{coin}/positioning` | `data:read` | Read |
| `wf_get_trade_markets_coin_tape` | `GET /v1/trade/markets/{coin}/tape` | `data:read` | Read |
| `wf_get_trade_markets_coin_history` | `GET /v1/trade/markets/{coin}/history` | `data:read` | Read |
| `wf_get_account_trade_watched_positions` | `GET /v1/account/trade/watched-positions` | `trade:read` | Read |
| `wf_get_account_trade_orders` | `GET /v1/account/trade/orders` | `trade:read` | Read |
| `wf_get_copy_capabilities` | `GET /v1/copy/capabilities` | `data:read` | Read |
| `wf_get_copy_engine_scope` | `GET /v1/copy/engine-scope` | `data:read` | Read |
| `wf_get_copy_portfolios` | `GET /v1/copy/portfolios` | `data:read` | Read |
| `wf_get_copy_shelves` | `GET /v1/copy/shelves` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug` | `GET /v1/copy/portfolios/{handle}/{slug}` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug_versions_version` | `GET /v1/copy/portfolios/{handle}/{slug}/versions/{version}` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug_copyability` | `GET /v1/copy/portfolios/{handle}/{slug}/copyability` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug_stats` | `GET /v1/copy/portfolios/{handle}/{slug}/stats` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug_exposure` | `GET /v1/copy/portfolios/{handle}/{slug}/exposure` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug_feed` | `GET /v1/copy/portfolios/{handle}/{slug}/feed` | `data:read` | Read |
| `wf_get_copy_portfolios_handle_slug_card` | `GET /v1/copy/portfolios/{handle}/{slug}/card` | `data:read` | Read |
| `wf_get_copy_creators_handle` | `GET /v1/copy/creators/{handle}` | `data:read` | Read |
| `wf_get_account_copy_capabilities` | `GET /v1/account/copy-capabilities` | `copy:read` | Read |
| `wf_get_account_copy_portfolios` | `GET /v1/account/copy-portfolios` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions` | `GET /v1/account/copy-subscriptions` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions_id_setup_precheck` | `GET /v1/account/copy-subscriptions/{id}/setup-precheck` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions_id_status` | `GET /v1/account/copy-subscriptions/{id}/status` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions_id_results` | `GET /v1/account/copy-subscriptions/{id}/results` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions_id_fills` | `GET /v1/account/copy-subscriptions/{id}/fills` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions_id_orders` | `GET /v1/account/copy-subscriptions/{id}/orders` | `copy:read` | Read |
| `wf_get_account_copy_subscriptions_id_decisions` | `GET /v1/account/copy-subscriptions/{id}/decisions` | `copy:read` | Read |
| `wf_get_account_copy_watches` | `GET /v1/account/copy-watches` | `copy:read` | Read |
| `wf_get_account_copy_creator` | `GET /v1/account/copy-creator` | `creator:read` | Read |
| `wf_get_account_copy_creator_portfolios` | `GET /v1/account/copy-creator/portfolios` | `creator:read` | Read |
| `wf_get_account_copy_creator_portfolios_id` | `GET /v1/account/copy-creator/portfolios/{id}` | `creator:read` | Read |
| `wf_get_account_copy_creator_leaders_address_returns` | `GET /v1/account/copy-creator/leaders/{address}/returns` | `creator:read` | Read |
| `wf_get_account_copy_creator_earnings` | `GET /v1/account/copy-creator/earnings` | `creator:read` | Read |
| `wf_get_account_copy_creator_statements` | `GET /v1/account/copy-creator/statements` | `creator:read` | Read |
| `wf_get_account_copy_creator_payout_identity` | `GET /v1/account/copy-creator/payout-identity` | `creator:read` | Read |
| `wf_get_account_copy_invoices` | `GET /v1/account/copy-invoices` | `copy:read` | Read |
| `wf_get_account_copy_invoices_id` | `GET /v1/account/copy-invoices/{id}` | `copy:read` | Read |

## Customer controls: unavailable in marketplace

Detailed input schemas: [customer-control-schema.json](customer-control-schema.json).

| Tool | HTTP operation | OAuth scope | Marketplace |
| --- | --- | --- | --- |
| `wf_post_account_wallets` | `POST /v1/account/wallets` | `wallets:write` | Dashboard only |
| `wf_patch_account_wallets_id` | `PATCH /v1/account/wallets/{id}` | `wallets:write` | Dashboard only |
| `wf_delete_account_wallets_id` | `DELETE /v1/account/wallets/{id}` | `wallets:write` | Dashboard only |
| `wf_post_account_wallet_siwe_challenge` | `POST /v1/account/wallet/siwe-challenge` | `trading-accounts:write` | Dashboard only |
| `wf_post_account_trading_accounts` | `POST /v1/account/trading-accounts` | `trading-accounts:write` | Dashboard only |
| `wf_post_account_trading_accounts_id_approvals_submitted` | `POST /v1/account/trading-accounts/{id}/approvals-submitted` | `trading-accounts:write` | Dashboard only |
| `wf_post_account_trading_accounts_id_disconnect` | `POST /v1/account/trading-accounts/{id}/disconnect` | `trading-accounts:write` | Dashboard only |
| `wf_post_account_trade_orders` | `POST /v1/account/trade/orders` | `trade:write` | Dashboard only |
| `wf_patch_account_trade_orders_id` | `PATCH /v1/account/trade/orders/{id}` | `trade:write` | Dashboard only |
| `wf_delete_account_trade_orders_id` | `DELETE /v1/account/trade/orders/{id}` | `trade:write` | Dashboard only |
| `wf_post_account_copy_subscriptions` | `POST /v1/account/copy-subscriptions` | `copy:write` | Dashboard only |
| `wf_patch_account_copy_subscriptions_id` | `PATCH /v1/account/copy-subscriptions/{id}` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_submit` | `POST /v1/account/copy-subscriptions/{id}/submit` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_discard` | `POST /v1/account/copy-subscriptions/{id}/discard` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_setup` | `POST /v1/account/copy-subscriptions/{id}/setup` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_start` | `POST /v1/account/copy-subscriptions/{id}/start` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_pause` | `POST /v1/account/copy-subscriptions/{id}/pause` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_resume` | `POST /v1/account/copy-subscriptions/{id}/resume` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_stop` | `POST /v1/account/copy-subscriptions/{id}/stop` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_close` | `POST /v1/account/copy-subscriptions/{id}/close` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_revoke` | `POST /v1/account/copy-subscriptions/{id}/revoke` | `copy:write` | Dashboard only |
| `wf_post_account_copy_subscriptions_id_excluded_markets` | `POST /v1/account/copy-subscriptions/{id}/excluded-markets` | `copy:write` | Dashboard only |
| `wf_put_account_copy_watches_id` | `PUT /v1/account/copy-watches/{id}` | `copy:write` | Dashboard only |
| `wf_delete_account_copy_watches_id` | `DELETE /v1/account/copy-watches/{id}` | `copy:write` | Dashboard only |
| `wf_post_account_copy_reports` | `POST /v1/account/copy-reports` | `copy:write` | Dashboard only |
| `wf_put_account_copy_creator` | `PUT /v1/account/copy-creator` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios` | `POST /v1/account/copy-creator/portfolios` | `creator:write` | Dashboard only |
| `wf_put_account_copy_creator_portfolios_id_draft` | `PUT /v1/account/copy-creator/portfolios/{id}/draft` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios_id_preview` | `POST /v1/account/copy-creator/portfolios/{id}/preview` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios_id_publish` | `POST /v1/account/copy-creator/portfolios/{id}/publish` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios_id_visibility` | `POST /v1/account/copy-creator/portfolios/{id}/visibility` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios_id_archive` | `POST /v1/account/copy-creator/portfolios/{id}/archive` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios_id_unarchive` | `POST /v1/account/copy-creator/portfolios/{id}/unarchive` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_portfolios_id_fee_schedule` | `POST /v1/account/copy-creator/portfolios/{id}/fee-schedule` | `creator:write` | Dashboard only |
| `wf_put_account_copy_creator_portfolios_id_affiliation` | `PUT /v1/account/copy-creator/portfolios/{id}/affiliation` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_leaders_check` | `POST /v1/account/copy-creator/leaders/check` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_payout_identity_challenge` | `POST /v1/account/copy-creator/payout-identity/challenge` | `creator:write` | Dashboard only |
| `wf_post_account_copy_creator_payout_identity_prove` | `POST /v1/account/copy-creator/payout-identity/prove` | `creator:write` | Dashboard only |

