# Research reads, cost and source meaning

Read the [operation index](api-operations.md) to select a tool. For exact accepted arguments, inspect [research-schema.json](research-schema.json) or the host's discovered input schema. The examples below show tool arguments, with the customer's wallet address substituted for `WALLET`.

## Prepared data first

`wf_get_wallet` accepts `{ "address": "WALLET" }` and costs 1 weight unit. Its account, positions, spot, metrics and profile sections are prepared observations. `{ "address": "WALLET", "query": { "include": "trades" } }` costs 5 and adds prepared analysis. Section tools are `wf_get_wallet_account`, `wf_get_wallet_positions`, `wf_get_wallet_spot`, `wf_get_wallet_metrics`, `wf_get_wallet_profile`, `wf_get_wallet_analysis` and `wf_get_wallet_trades`. The first five cost 1; analysis and trades cost 5. Cache hits and HTTP 304 responses still cost weight.

Use `query.period` (`24H`, `7D`, `30D`, `90D`, `ALL`) for metrics/analysis. Account/profile accept no query. Positions accept `coin`, `dex`, `limit`, `cursor`; spot accepts `token`, `limit`, `cursor`; trades adds `status` (`open` or `closed`) to the positions filters. Lists default to 50 and cap at 100. `dex:""` selects the main DEX; omitted `dex` leaves all retained DEXes. Exact case-sensitive market filters keep their original market names.

Prepared cursors bind wallet, section, filters, page size and source document hash. Pass `next_cursor` unchanged with the same query. If a snapshot changed, restart without the cursor and replace the old pages. Positions, balances and modeled trades are bounded retained lists. A null analysis or unindexed wallet cannot establish no trading activity.

## Screener

Use `wf_get_wallet_screener` to select a small cohort before detailed reads. Example:

```json
{
  "query": {
    "period": "30D",
    "sort": "fill_realized_usd",
    "dir": "desc",
    "limit": 10,
    "fields": ["total_assets_usd", "fill_realized_usd", "fees_usd", "trader_score"],
    "filters": { "trade_count": { "min": "20" } }
  }
}
```

All filter bounds remain strings. `fields` is an array in the MCP; the adapter encodes the API's comma-separated field list. `filters` encodes inclusive `min.<column>`/`max.<column>` bounds. Use only the discovered columns. Do not sort by unavailable ROI or present a screener ranking as a qualified copy-return comparison.

The page size is 1–500, default 25. Weight is `max(5, ceil(limit/25))`; a plan's burst allowance may impose a smaller usable page. Filters combine with AND and null filtered values do not match. Preserve the period, sort, direction and filters across a cursor; fields/page size may change. `409 DIRECTORY_SNAPSHOT_CHANGED` requires a new first page. `SCREENER_COLUMN_UNAVAILABLE` requires a supported field or an explicit unavailable result, never a fabricated zero.

## Public venue observations

`wf_get_wallet_open_orders`, `wf_get_wallet_order_history`, `wf_get_wallet_fills`, `wf_get_wallet_funding`, `wf_get_wallet_transfers`, `wf_get_wallet_vaults`, `wf_get_wallet_staking` and `wf_get_wallet_portfolio` each cost 5. These are bounded reads through WalletFollow's allowlisted public information proxy. Transfers, vaults and staking tools never execute an action. Native fills are distinct from the prepared round-trip trades.

Lists default to 50 and cap at 100. `offset` is 0–1999 inside the retained source response. After page one, send its `source_response_sha256` as `query.snapshot`, its `pagination.next_offset` as `query.offset`, and the same filters/window. A changed snapshot requires restarting. `available` counts retained matching rows, not lifetime events.

Fills, funding and transfers accept `start_ms`/`end_ms` as integer epoch milliseconds. End must not be in the future; start precedes end and the range is at most 31 days. Defaults select 24 hours. Reuse the returned `requested_window` across pages. `query.kind:"twap"` selects latest retained TWAP slices; it does not unlock arbitrary historical TWAP pagination. Deduplicate ordinary/TWAP fills by native fill identity when combining them.

Staking selects exactly one `query.part`: `summary`, `delegations`, `history`. Summary accepts no list filters. Portfolio accepts a native `family` (`day`, `week`, `month`, `allTime`, `perpDay`, `perpWeek`, `perpMonth`, `perpAllTime`) and `points` (1–2000, default 500). It returns original selected points and source counts; missing families stay missing, and downsampled observations are not a reconstructed continuous equity curve.

`wf_get_markets_coin_candles` takes a top-level exact `coin` and requires `query.interval`. Intervals are `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `2h`, `4h`, `8h`, `12h`, `1d`, `3d`, `1w`, `1M`. Its time range is at most 31 days and must fit 2000 candles. Return OHLC/volume strings with the original source time; an observation does not authorize a market order.

## Freshness and quota

Keep `freshness`, per-section clocks, `gaps`, coverage status, pagination/truncation and native decimal strings. Prepared cache status is distinct from the source's observation age. Live `freshness.status:"UNKNOWN"` with `as_of_ms:null` must stay unknown; never replace it with the request time. Even `RECENT` refers to proxy observation time, not an execution guarantee. Bounded observation coverage is explicitly incomplete. Retained chart PnL, fill PnL, modeled trade PnL and copy ROI are different measures.

`wf_get_usage`, `wf_get_catalog` and `wf_get_openapi_json` are weight-zero metadata with a separate finite rate limit. API weights share the customer plan across credentials. Use returned usage/rate/quota headers when provided. Upstream failures and API refusals normally report zero request weight; do not promise a refund if its acknowledgement is uncertain. `429` carries a retry delay; monthly exhaustion may require waiting for the reset or changing a plan through the dashboard. Do not start an unbounded background poll or hidden multi-window crawl.

Weight-zero metadata is still an authenticated read attempt: catalog and OpenAPI count toward a configured per-key daily request ceiling; usage is excluded. Admitted reads that fail consume the ceiling, writes are excluded, and rotation keeps the credential’s UTC-day counter. `KEY_DAILY_LIMIT` requires waiting for the returned UTC reset delay or a deliberate dashboard policy change; do not swap keys to evade it.
