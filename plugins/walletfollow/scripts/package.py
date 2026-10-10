#!/usr/bin/env python3
"""Validate and archive this plugin only; never reads credentials or the monorepo."""
from __future__ import annotations

import argparse
import json
import re
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MCP_URL = "https://mcp.walletfollow.ai/mcp"
REQUIRED = {
    "plugin.json", "mcp.json", ".mcp.json", ".claude-plugin/plugin.json",
    "README.md", "LICENSE", "assets/walletfollow.svg", "scripts/package.py",
    "skills/walletfollow-connect/SKILL.md",
    "skills/walletfollow-connect/agents/openai.yaml",
    "skills/walletfollow-research/SKILL.md",
    "skills/walletfollow-research/agents/openai.yaml",
    "skills/walletfollow-research/references/research.md",
    "skills/walletfollow-research/references/customer.md",
    "skills/walletfollow-research/references/api-operations.md",
    "skills/walletfollow-research/references/research-schema.json",
    "skills/walletfollow-research/references/customer-read-schema.json",
    "skills/walletfollow-research/references/customer-control-schema.json",
    "review-cases.json",
}
SECRET = re.compile(r"(?:aperi_[A-Za-z0-9_-]{43}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")


def validate() -> list[Path]:
    files: list[Path] = []
    for entry in ROOT.rglob("*"):
        info = entry.lstat()
        if stat.S_ISLNK(info.st_mode):
            raise ValueError("Symlink refused in plugin")
        if stat.S_ISDIR(info.st_mode):
            continue
        if not stat.S_ISREG(info.st_mode):
            raise ValueError("Non-regular plugin file refused")
        relative = entry.relative_to(ROOT).as_posix()
        if relative not in REQUIRED:
            raise ValueError(f"Unexpected plugin file: {relative}")
        if info.st_size > 256 * 1024:
            raise ValueError(f"File exceeds review size bound: {relative}")
        content = entry.read_text(encoding="utf-8")
        if SECRET.search(content):
            raise ValueError("Literal credential pattern refused")
        if entry.suffix == ".json":
            json.loads(content)
        files.append(entry)
    if {entry.relative_to(ROOT).as_posix() for entry in files} != REQUIRED:
        raise ValueError("Plugin has missing required files")

    manifests = [json.loads((ROOT / name).read_text()) for name in ["plugin.json", ".claude-plugin/plugin.json"]]
    if any(manifest["name"] != "walletfollow" or manifest["version"] != manifests[0]["version"] for manifest in manifests):
        raise ValueError("Plugin manifest identities differ")
    for name, transport in [("mcp.json", "streamable-http"), (".mcp.json", "http")]:
        servers = json.loads((ROOT / name).read_text())["mcpServers"]
        if set(servers) != {"walletfollow"} or servers["walletfollow"]["url"] != MCP_URL or servers["walletfollow"]["type"] != transport:
            raise ValueError("Pinned MCP connection differs")
        if set(servers["walletfollow"]) - {"type", "url", "oauth"}:
            raise ValueError("Unexpected MCP transport/credential fields")
    claude = json.loads((ROOT / ".mcp.json").read_text())["mcpServers"]["walletfollow"]
    if claude.get("oauth") != {"scopes": "data:read offline_access"}:
        raise ValueError("Baseline OAuth scope differs")
    operations = []
    ref = ROOT / "skills/walletfollow-research/references"
    for name in ["research-schema", "customer-read-schema", "customer-control-schema"]:
        operations.extend(json.loads((ref / f"{name}.json").read_text())["operations"])
    if len(operations) != 100 or sum(operation["method"] == "GET" for operation in operations) != 62:
        raise ValueError("API operation inventory differs")
    if len({operation["tool"] for operation in operations}) != len(operations):
        raise ValueError("API tool identities overlap")
    if any(operation["marketplace_available"] != (operation["method"] == "GET") for operation in operations):
        raise ValueError("Marketplace operation boundary differs")
    if any(len(operation["tool"]) > 64 or not operation["path"].startswith("/v1/") for operation in operations):
        raise ValueError("Invalid API operation identity")
    return sorted(files, key=lambda entry: entry.relative_to(ROOT).as_posix())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.check == (args.output is not None):
        parser.error("Choose exactly one of --check or --output")
    files = validate()
    if args.output is not None:
        output = args.output.resolve()
        if output.is_relative_to(ROOT):
            raise ValueError("Write the ZIP outside the plugin")
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
            for entry in files:
                member = zipfile.ZipInfo(entry.relative_to(ROOT).as_posix(), (1980, 1, 1, 0, 0, 0))
                member.create_system = 3
                member.external_attr = (stat.S_IFREG | 0o644) << 16
                member.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(member, entry.read_bytes())
        with zipfile.ZipFile(output) as archive:
            if archive.testzip() is not None or set(archive.namelist()) != REQUIRED:
                raise ValueError("Archive readback failed")
    print(json.dumps({"status": "PASS", "files": len(files), "archive": str(args.output) if args.output else None}))


if __name__ == "__main__":
    main()
