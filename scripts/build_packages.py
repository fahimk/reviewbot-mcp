#!/usr/bin/env python3
"""Build explicit, credential-free plugin archives without network access."""
from pathlib import Path
import hashlib
import json
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "plugin.json", "mcp.json", ".mcp.json", ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json", "server.json", "README.md", "LICENSE",
    "assets/icon.png", "skills/weekly-review-brief/SKILL.md",
    "skills/draft-review-replies/SKILL.md", "docs/tools.md",
    "docs/package-notes.md", "docs/reviewer-scenarios.md",
    "docs/submission-tracker.md", "scripts/build_packages.py",
    "submission/mcp.openai.json",
)


def main():
    version = json.loads((ROOT / "plugin.json").read_text())["version"]
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    for variant in ("portable", "openai"):
        archive = dist / f"reviewbot-{version}-{variant}.zip"
        with ZipFile(archive, "w", ZIP_DEFLATED) as package:
            for relative in FILES:
                source = ROOT / relative
                if variant == "openai" and relative == "mcp.json":
                    source = ROOT / "submission/mcp.openai.json"
                if not source.is_file() or source.is_symlink():
                    raise ValueError(f"Missing or symlinked package file: {relative}")
                package.writestr(relative, source.read_bytes())
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        print(f"{archive.name}  sha256:{digest}")


if __name__ == "__main__":
    main()
