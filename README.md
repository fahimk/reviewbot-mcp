# ReviewBot MCP and plugins

ReviewBot brings reviews collected from your monitored App Store and Google Play apps into an assistant. Search feedback, inspect individual reviews, summarize an observed review sample, and draft replies for your team to review.

Version **0.1.0** is a release candidate. Hosted production verification and directory submissions are in progress. See the [submission tracker](docs/submission-tracker.md) for current status before connecting.

## Connect

- Remote MCP URL: `https://api.reviewbot.io/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth through ReviewBot; use the client's connection flow.
- Account: an existing eligible paid or trial ReviewBot account with monitored App Store or Google Play apps.
- Planned server documentation: `https://api.reviewbot.io/mcp/docs`

In a client that supports remote OAuth MCP servers, add the URL above and complete ReviewBot authorization. Never paste passwords, access tokens, or client secrets into a conversation or this repository. Account and organization settings may control which custom connectors can be added.

### Claude

For a custom connector, add the remote MCP URL in Claude's connector settings, then complete OAuth. The connection provides the tools; the plugin package also provides the two skills below.

To inspect the local Claude Code plugin after downloading this package:

```sh
claude plugin validate /absolute/path/to/reviewbot-mcp
claude --plugin-dir /absolute/path/to/reviewbot-mcp
```

Complete connection authorization in the host before calling tools. Add the included marketplace with `/plugin marketplace add fahimk/reviewbot-mcp`, followed by `/plugin install reviewbot@reviewbot`. The hosted endpoint must be live before you can connect.

### ChatGPT and Codex

This package uses the portable Agent Plugins format: root `plugin.json`, `mcp.json`, and `skills/`. Once the endpoint is deployed, a developer can add it through ChatGPT's **Plugins → Add custom MCP server** flow and test the connection. Public directory installation becomes available only after submission, review, and publication.

OpenAI's current packaging documentation adds OAuth metadata that the portable MCP 1.0.0 schema does not yet accept. The portable file stays schema-valid; `submission/mcp.openai.json` is the documented OpenAI submission variant. See [package notes](docs/package-notes.md) before uploading either archive. Neither format has yet been tested in the actual Claude or ChatGPT client.

## Tools and workflows

| Tool | Purpose |
| --- | --- |
| `list_apps` | List supported apps accessible to the connected account. |
| `search_reviews` | Find collected reviews using app, date, rating, locale, text, and version filters. |
| `get_review` | Read one accessible review by its returned review ID. |
| `get_review_stats` | Read counts and rating statistics for a bounded collected-review sample. |

The bundled `weekly-review-brief` skill creates a brief with statistics, recurring themes, source references, and coverage limits. The `draft-review-replies` skill prepares grounded reply drafts. All four tools are read-only. Replies are never published through this integration; use the returned ReviewBot dashboard link to continue in the existing reply flow when available.

Example requests:

- “Which of my apps can ReviewBot access?”
- “Summarize the reviews collected for my app over the last seven days.”
- “Draft replies to the latest three one-star reviews, without promising fixes.”

## Understand the data

Review windows use **collection time (`scannedAt`)**, not the date a reviewer posted. Each query supports at most 30 days. Search returns at most 50 reviews per page and scans at most 500 records per query. Statistics use the bounded observed sample, not the entire app-store population. Filters can produce incomplete coverage when the scan cap is reached.

Responses report coverage and freshness. Check `coverage.truncated`, `coverage.completeForWindow`, and `coverage.note` before drawing conclusions. A following cursor can retrieve another result page; it does not remove the server's scan bound. Unknown ratings, versions, and locales remain unknown. See the [tool reference](docs/tools.md) for the input contract and interpretation rules.

## Release checks

The server implementation has passed interoperability checks with the official MCP SDK client in legacy and pinned `2026-07-28` protocol modes, including the four tools and bounded inputs. This is not evidence of successful OAuth or tool use in an actual Claude or ChatGPT session. Those host tests, live endpoint verification, and directory review remain pending. Track them in [submission status](docs/submission-tracker.md).

This repository contains connection metadata, skills, documentation, and a brand asset. It contains no backend source, customer review exports, or credentials. Package code and documentation are MIT licensed; ReviewBot names and artwork remain their owners' trademarks and are not licensed by MIT.

[ReviewBot](https://reviewbot.io/) · [Support](https://reviewbot.io/contact/) · [Privacy](https://reviewbot.io/privacy/) · [Terms](https://reviewbot.io/terms/)
