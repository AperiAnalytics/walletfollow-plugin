---
name: walletfollow-connect
description: Connect or troubleshoot the WalletFollow research plugin in Claude or Codex, including OAuth, API permissions and quota errors. Use when a user wants to install, authenticate or restore this connection.
---

Connect the plugin's remote MCP at `https://mcp.walletfollow.ai/mcp` using the host's OAuth flow. Use [the connection guide](https://mcp.walletfollow.ai/) for the current account availability and browser setup.

Authentication occurs in the browser on the pinned `mcp.walletfollow.ai` origin. If setup requires an existing WalletFollow API key, the customer enters it only in that HTTPS consent form. Never request a key, token, password, private key, seed phrase or signature in chat, a tool argument, a shell command or a file. Do not reuse the operator's credentials for another customer. Plugin installation alone grants no API authority.

Start authorization with only `data:read` and `offline_access`. After the host completes authorization, call `wf_get_usage` to verify the connection and current plan. Verified-user research access depends on the current rollout; optional customer account reads retain their separate pilot restriction and need both the matching OAuth read scope and the key's existing live account permission. For an `insufficient_scope` challenge, request only its exact allowed read scope and have the customer authorize it in the browser. This package pins Claude to the baseline: add that read scope to the connection's OAuth scopes before reauthorizing; a plain reconnect will keep the pin. Codex can request it with `codex mcp login walletfollow --scopes data:read,offline_access,<required-read-scope>`. Never add write scopes. Reconnecting cannot create a trading permission or bypass an account restriction.

In the account API tab, the customer can set key expiry, exact IP restrictions and a daily read-request ceiling, rotate or revoke a key, and review or revoke individual MCP connections. Rotation does not reset the ceiling. IP restrictions apply to the assistant host’s network as well as browser authorization; cloud-hosted assistants may change their egress address. Never ask a user to disable a restriction automatically. A revoked connection or refresh-token replay requires fresh browser authorization.

For `KEY_DAILY_LIMIT` (`429`), explain the customer-selected ceiling and the UTC reset time; the customer can inspect usage or deliberately edit their own limit in the dashboard. This is a request ceiling, not a spending guarantee. Do not retry before the returned reset delay or suggest another key to evade it.

For `401`, reconnect or have the customer check credential expiry/revocation in [WalletFollow](https://walletfollow.ai/account). For `403`, explain the reported pilot, plan, scope or account restriction. For `429` or transient `503`, use the returned retry delay and a bounded retry; do not repeatedly reconnect or swap keys to avoid limits. Retain only the sanitized request ID and error code when reporting a problem through [support](https://mcp.walletfollow.ai/support).

Then use the bundled `walletfollow-research` skill for wallet, market, portfolio or owned-account research. The public plugin exposes read tools only. Trade execution, copying changes, wallet approvals and creator mutations belong in the customer's dashboard; OAuth does not enable them here.
