# Package formats and validation

ReviewBot App Reviews uses the plugin identifier `reviewbot-app-reviews` in the portable and Claude formats. Both formats share the same two skills. The MCP connection key remains `reviewbot`, and the registry namespace remains `io.github.fahimk/reviewbot`.

| File | Consumer |
| --- | --- |
| `plugin.json` | Portable Agent Plugins identity in a format supported by Cursor, with OpenAI listing/review metadata. |
| `mcp.json` | Canonical Agent Plugins 1.0.0 remote connection, including Cursor's portable-plugin path. |
| `.claude-plugin/plugin.json` | Claude plugin identity. |
| `.claude-plugin/marketplace.json` | Single-plugin Claude marketplace from the public repository. |
| `.mcp.json` | Claude HTTP connection configuration. |
| `server.json` | Official MCP Registry remote entry, active at version 0.1.0. |
| `submission/mcp.openai.json` | OpenAI submission variant with discovery-based OAuth DCR metadata. |

## OpenAI auth metadata difference

As checked on 2026-11-04, [OpenAI's packaging documentation](https://developers.openai.com/plugins/build/plugins#use-automatic-oauth-client-registration) places OAuth configuration at `mcpServers.reviewbot.extensions.com.openai.auth`. The [portable MCP 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json) disallows per-server `extensions`. The primary `mcp.json` follows the portable schema. The separate OpenAI file follows the documented OpenAI OAuth format. On 2026-11-09, the original version 0.1.0 OpenAI archive uploaded successfully and the listing was submitted for review. This resolves the earlier `Invalid URL` upload blocker; it does not imply directory approval or portable-schema compatibility for the OpenAI variant.

Download versioned archives from [GitHub Releases](https://github.com/fahimk/reviewbot-mcp/releases). The `reviewbot-app-reviews-VERSION-portable.zip` archive includes the canonical `mcp.json`; `reviewbot-app-reviews-VERSION-openai.zip` uses the OpenAI submission variant instead. The archives contain only plugin manifests, skills, documentation, and the icon; maintainer packaging utilities are not shipped. The public submission variant is included for reference. The OpenAI variant has no embedded secret and relies on server OAuth discovery and dynamic client registration. The live production service passed that OAuth flow in the synthetic canary.

The OpenAI manifest intentionally omits reviewer credentials, reviewer-only instructions, a demo URL, and published identity IDs. Review materials and access details belong in the secure submission dashboard, not in a package or this repository.

## Cursor and Glama

Cursor supports the existing portable package format. This documentation update does not modify its manifests, skills, version 0.1.0 release tag, or published archives. Cursor-specific components are unnecessary for these two skills and one remote server. Actual Cursor import and OAuth behavior still need host testing, and Marketplace commercial eligibility needs clarification before submission; see the [submission handoff](cursor-glama-submission.md).

Glama's hosted-endpoint connector route points to the existing service. It does not require a runtime package or imply that the hosted backend is open source. Its authenticated test profile is separate from public listing metadata.

## Checks

Run the portable manifests and registry manifest against their declared schemas, then run Skill Creator's `quick_validate.py` on each skill. `claude plugin validate .` provides local Claude package validation. These checks validate packaging, not OAuth completion, live tool behavior, directory acceptance, or installation in a client.

The backend passed staging and production OAuth/tool canaries and official MCP SDK checks in legacy and pinned `2026-07-28` modes. The unmodified Docker MCP Gateway passed initialization, exact tool listing, and all four tool calls using a short-lived OAuth access token. Docker CLI browser login/credential storage remains unverified. The [review scenarios](reviewer-scenarios.md) define exactly five positive and three negative cases.

On 2026-11-04, live Claude and ChatGPT custom MCP sessions completed OAuth and returned the expected synthetic sample: three collected reviews, two rated, one unknown rating, and a 3.0 average among rated reviews. Tests used matching explicit UTC windows, read review detail, treated the instruction-like test review as data, and retrieved distinct pages with unchanged filters while preserving incomplete-page coverage. ChatGPT's brief and draft passed; transient response-display errors cleared after reloading the response. Claude's initial generic-prompt draft invented an internal handoff, then passed after an explicit prohibition on unconfirmed actions, including a fresh-session starter-prompt check. Both hosts explained read-only access and manual reply handoff. Those two test grants were revoked through ReviewBot afterward; the separate OpenAI review connection retained on 2026-11-09 is tracked in the [submission status](submission-tracker.md). These were custom-connection prompt workflows; packaged skill installation remains unverified, and passing samples do not guarantee every generated draft is accurate.

The registry entry deliberately omits `repository`: this is a thin integration package, not the hosted backend's source repository. Add a repository field only if its meaning and public availability are accurate. The [published registry record](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.fahimk%2Freviewbot/versions/0.1.0) confirms `io.github.fahimk/reviewbot` version `0.1.0` is active. Registry publication does not establish approval in another directory.

Primary references: [Agent Plugins](https://agent-plugins.org/), [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [Claude manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference), [MCP remote servers](https://modelcontextprotocol.io/registry/remote-servers), [registry authentication](https://modelcontextprotocol.io/registry/authentication).
