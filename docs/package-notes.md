# Package formats and validation

ReviewBot App Reviews uses the plugin identifier `reviewbot-app-reviews` in the portable and Claude formats. Both formats share the same two skills. The MCP connection key remains `reviewbot`, and the registry namespace remains `io.github.fahimk/reviewbot`.

| File | Consumer |
| --- | --- |
| `plugin.json` | Portable Agent Plugins identity and OpenAI listing/review metadata. |
| `mcp.json` | Canonical Agent Plugins 1.0.0 remote connection. |
| `.claude-plugin/plugin.json` | Claude plugin identity. |
| `.claude-plugin/marketplace.json` | Single-plugin Claude marketplace from the public repository. |
| `.mcp.json` | Claude HTTP connection configuration. |
| `server.json` | Official MCP Registry remote entry, active at version 0.1.0. |
| `submission/mcp.openai.json` | OpenAI submission variant with discovery-based OAuth DCR metadata. |

## OpenAI auth metadata difference

As checked on 2026-11-04, [OpenAI's packaging documentation](https://developers.openai.com/plugins/build/plugins#use-automatic-oauth-client-registration) places OAuth configuration at `mcpServers.reviewbot.extensions.com.openai.auth`. The [portable MCP 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json) disallows per-server `extensions`. The primary `mcp.json` follows the portable schema. The separate OpenAI file follows the documented OpenAI OAuth format and must be checked by the actual upload/scan flow. The attempted upload stopped at developer identity verification, before any file was uploaded. This variant is not claimed to pass the portable schema or the OpenAI portal scan.

Download versioned archives from [GitHub Releases](https://github.com/fahimk/reviewbot-mcp/releases). The `reviewbot-app-reviews-VERSION-portable.zip` archive includes the canonical `mcp.json`; `reviewbot-app-reviews-VERSION-openai.zip` uses the OpenAI submission variant instead. The archives contain only plugin manifests, skills, documentation, and the icon; maintainer packaging utilities are not shipped. The public submission variant is included for reference. The OpenAI variant has no embedded secret and relies on server OAuth discovery and dynamic client registration. The live production service passed that OAuth flow in the synthetic canary.

The OpenAI manifest intentionally omits reviewer credentials, reviewer-only instructions, a demo URL, and published identity IDs. Add a real reviewer-accessible demo and enter access details only in the secure dashboard. Do not fabricate them or put credentials in a package. The developer name and category must be confirmed against the selected verified identity and available dashboard categories.

## Checks

Run the portable manifests and registry manifest against their declared schemas, then run Skill Creator's `quick_validate.py` on each skill. `claude plugin validate .` provides local Claude package validation. These checks validate packaging, not OAuth completion, live tool behavior, directory acceptance, or installation in a client.

The backend passed staging and production OAuth/tool canaries and official MCP SDK checks in legacy and pinned `2026-07-28` modes. The unmodified Docker MCP Gateway passed initialization, exact tool listing, and all four tool calls using a short-lived OAuth access token. Docker CLI browser login/credential storage and actual Claude/ChatGPT tool-and-skill sessions remain unverified. The [review scenarios](reviewer-scenarios.md) define exactly five positive and three negative cases.

The registry entry deliberately omits `repository`: this is a thin integration package, not the hosted backend's source repository. Add a repository field only if its meaning and public availability are accurate. The [published registry record](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.fahimk%2Freviewbot/versions/0.1.0) confirms `io.github.fahimk/reviewbot` version `0.1.0` is active. Registry publication does not establish approval in another directory.

Primary references: [Agent Plugins](https://agent-plugins.org/), [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [Claude manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference), [MCP remote servers](https://modelcontextprotocol.io/registry/remote-servers), [registry authentication](https://modelcontextprotocol.io/registry/authentication).
