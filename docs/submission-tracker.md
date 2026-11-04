# Submission tracker

Updated 2026-11-04. The public repository is being released; directory submissions are pending. A prepared manifest, successful validation, or accessible submission form is not an accepted listing.

| Channel | Status | Actionable path | Remaining prerequisites |
| --- | --- | --- | --- |
| Public package repository | Created | [fahimk/reviewbot-mcp](https://github.com/fahimk/reviewbot-mcp) | Versioned release follows hosted verification. The repository contains integration metadata, not hosted backend source. |
| Official MCP Registry | Not submitted | `mcp-publisher login github`, then `mcp-publisher publish` from this directory when ready | Publicly reachable remote endpoint, working OAuth discovery, live smoke test, verified `fahimk` namespace, and final `server.json`. No npm package is needed for this remote-only entry. Registry remains in preview. |
| Claude connector directory | Not submitted | [Developer portal](https://claude.ai/directory/manage) → new MCP connector | Add and successfully test the custom connector, complete its connector submission and requested review materials. Verify OAuth, read-only annotations, links, and accessible test data. |
| Claude plugin directory | Not submitted | [Developer portal](https://claude.ai/directory/manage) → new plugin from GitHub | Connect an authorized GitHub account, provide the plugin repository, pass validation/review, and make it public before listing publication. The remote MCP service also needs its connector submission. |
| OpenAI shared ChatGPT/Codex directory | Not submitted | [Developer dashboard](https://platform.openai.com/plugins) → plugin upload and review | Select a verified developer identity, test the custom MCP connection, scan the OpenAI archive, resolve any auth/schema issue, supply a real demo, and enter reviewer access only in the secure portal. Run all eight cases in the actual host. |
| Glama | Not submitted | [MCP servers](https://glama.ai/mcp/servers) → Add Server | Sign-in/account access is needed. Verify eligibility for a hosted service whose public repository is only an integration package; do not call the proprietary backend open source. Provide the final URL/repository only when live. |

## Readiness evidence

- Portable/Claude/registry package checks: recorded separately by the local validator, not directory approval.
- Official MCP SDK client interoperability: backend checks passed in legacy and pinned `2026-07-28` modes for the four tools and bounded inputs.
- Public endpoint and OAuth discovery after deployment: pending.
- Actual Claude OAuth connection and tool/skill scenarios: pending.
- Actual ChatGPT OAuth connection and tool/skill scenarios: pending.
- Reviewer-accessible demo recording: pending.
- Secure reviewer account/access details: pending; never store them here.
- Publication/approval URLs or registry receipts: none.

## Registry preparation

The [official quickstart](https://modelcontextprotocol.io/registry/quickstart) documents `mcp-publisher` installation through Homebrew or official release binaries. The latest release inspected on 2026-11-04 was [v1.8.7](https://github.com/modelcontextprotocol/registry/releases/tag/v1.8.7). A safe local preparation path is a version-pinned official binary, verified against its published SHA-256, extracted into a task-local tools directory rather than installed globally. Checking `--help` is not authentication or publication.

Authenticate with the intended GitHub account using the [documented device flow](https://modelcontextprotocol.io/registry/authentication). It controls the `io.github.fahimk/` namespace. Keep generated tokens and authentication files outside the public package. Do not rerun initialization over the prepared `server.json`. Inspect the publisher's current help and validation output before the actual publish step; stop if it would overwrite a conflicting existing identity or version.

The registry hosts discovery metadata, not the hosted service or its payments. [Remote entries](https://modelcontextprotocol.io/registry/remote-servers) require a publicly accessible URL. A server may require OAuth for account data; it must still expose the discovery/authorization flow required by its clients. This package intentionally has no registry `repository` claim for unpublished backend source.

## Submission references

- [Claude plugin submission](https://claude.com/docs/plugins/submit): repository access, validation, review, and publication are separate steps.
- [OpenAI submission](https://developers.openai.com/plugins/deploy/submission): exact five positive/three negative MCP cases and a real demo are review requirements; upload alone is insufficient.
- [OpenAI packaging](https://developers.openai.com/plugins/build/plugins): portable format and OAuth metadata.
- [Glama MCP directory](https://glama.ai/mcp/servers): Add Server is the observed entry point; account access and fit still need confirmation.

No paid listing, account creation, star, directory submission, or public announcement is part of this prepared package.
