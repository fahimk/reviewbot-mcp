# Package formats and validation

The same two skills are shared by the portable and Claude formats.

| File | Consumer |
| --- | --- |
| `plugin.json` | Portable Agent Plugins identity and OpenAI listing/review metadata. |
| `mcp.json` | Canonical Agent Plugins 1.0.0 remote connection. |
| `.claude-plugin/plugin.json` | Claude plugin identity. |
| `.claude-plugin/marketplace.json` | Single-plugin Claude marketplace, usable after repository publication. |
| `.mcp.json` | Claude HTTP connection configuration. |
| `server.json` | Official MCP Registry remote entry, not yet published. |
| `submission/mcp.openai.json` | OpenAI submission variant with discovery-based OAuth DCR metadata. |

## OpenAI auth metadata difference

As checked on 2026-11-04, [OpenAI's packaging documentation](https://developers.openai.com/plugins/build/plugins#use-automatic-oauth-client-registration) places OAuth configuration at `mcpServers.reviewbot.extensions.com.openai.auth`. The [portable MCP 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json) disallows per-server `extensions`. The primary `mcp.json` follows the portable schema. The separate OpenAI file follows the documented OpenAI OAuth format and must be checked by the actual upload/scan flow. It is not claimed to pass the portable schema.

`python3 scripts/build_packages.py` produces two archives under `dist/`. The portable archive includes the canonical `mcp.json`; the OpenAI archive replaces that file with the submission variant. Both use an explicit allowlist and exclude validation environments, credentials, and customer data. The public submission variant is included for reproducibility. The OpenAI variant has no embedded secret and relies on server OAuth discovery and dynamic client registration. Confirm the live server advertises and supports that flow before submission.

The OpenAI manifest intentionally omits reviewer credentials, reviewer-only instructions, a demo URL, and published identity IDs. Add a real reviewer-accessible demo and enter access details only in the secure dashboard. Do not fabricate them or put credentials in a package. The developer name and category must be confirmed against the selected verified identity and available dashboard categories.

## Checks

Run the portable manifests and registry manifest against their declared schemas, then run Skill Creator's `quick_validate.py` on each skill. `claude plugin validate .` provides local Claude package validation. These checks validate packaging, not OAuth completion, live tool behavior, directory acceptance, or installation in a client.

The backend has been checked with the official MCP SDK client in legacy and pinned `2026-07-28` modes. Actual Claude and ChatGPT session tests remain pending, including OAuth connection, reconnection, revocation, denied access, empty results, bounded/truncated results, and both skill workflows. The [review scenarios](reviewer-scenarios.md) define exactly five positive and three negative cases.

The registry entry deliberately omits `repository`: this is a thin integration package, not the hosted backend's source repository. Add a repository field only if its meaning and public availability are accurate. `io.github.fahimk/reviewbot` requires authentication to the corresponding GitHub namespace before publishing; a local file is not a registry listing.

Primary references: [Agent Plugins](https://agent-plugins.org/), [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [Claude manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference), [MCP remote servers](https://modelcontextprotocol.io/registry/remote-servers), [registry authentication](https://modelcontextprotocol.io/registry/authentication).
