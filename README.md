# WalletFollow research plugin

Research Hyperliquid wallets, markets, published copy portfolios and permitted own-account reports through WalletFollow’s hosted OAuth MCP. This repository contains the plugin package and its Claude/Codex marketplace manifests; the hosted API and account data are outside this repository.

The plugin includes two skills, one remote server at `https://mcp.walletfollow.ai/mcp`, and a reference for all 100 API operations. The marketplace exposes 62 GET tools. Its 38 financial/customer mutations stay in the WalletFollow dashboard. Authorization begins with only `data:read` and `offline_access`; private reports need exact optional read scopes, existing API permissions and the current account eligibility.

Website: [walletfollow.ai](https://walletfollow.ai) · [MCP setup and documentation](https://walletfollow.ai/mcp).

## Install

Claude Code:

```sh
claude plugin marketplace add AperiAnalytics/walletfollow-plugin
claude plugin install walletfollow@walletfollow-plugins
```

Codex:

```sh
codex plugin marketplace add AperiAnalytics/walletfollow-plugin --ref main
codex plugin add walletfollow@walletfollow-plugins
```

For Claude chat/Cowork, install the plugin ZIP through Customize → Plugins or use an approved directory listing when available. A custom connector alone supplies MCP tools; the bundle adds the research skills. Authenticate in your client’s browser OAuth flow. Enter an existing API credential only on the HTTPS consent page at `mcp.walletfollow.ai`, never in chat, tool arguments or a manifest.

Use [the connection guide](https://mcp.walletfollow.ai/) for current availability and client setup. See [the complete package README](plugins/walletfollow/README.md), [privacy notice](https://mcp.walletfollow.ai/privacy), [service terms](https://mcp.walletfollow.ai/terms) and [support](https://mcp.walletfollow.ai/support). Directory listing and approval are separate from installation through this repository.

## Validate and build

```sh
claude plugin validate plugins/walletfollow --strict
claude plugin validate .claude-plugin/marketplace.json --strict
python3 plugins/walletfollow/scripts/package.py --check
python3 plugins/walletfollow/scripts/package.py --output /tmp/walletfollow-1.0.0.zip
```

The builder uses Python’s standard library and makes a deterministic plugin-only ZIP. Keep the ZIP outside the plugin folder. It checks the exact file inventory, read-only marketplace boundary and pinned connection, and refuses embedded API credentials or symlinks. The plugin installs no dependencies, runs no hooks and starts no local server.

The [MIT license](LICENSE) applies to this plugin package; it grants no license to the hosted service, account data or unrelated WalletFollow source. Support contact: `info@walletfollow.ai`; the owner is provisioning the mailbox and will verify delivery before directory submission.
