# ReviewBot App Reviews

ReviewBot brings reviews collected from your monitored App Store and Google Play apps into an assistant. Search feedback, inspect individual reviews, summarize an observed review sample, and draft replies for your team to review.

[Get started with ReviewBot MCP](https://reviewbot.io/mcp/) for setup steps, example workflows, and account requirements.

The hosted service is live, and version **0.1.0** is active in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.fahimk%2Freviewbot/versions/0.1.0). OpenAI and Claude directory submissions are in review; the Docker catalog contribution remains open. See the [submission tracker](docs/submission-tracker.md) for availability in each directory.

## Connect

- Remote MCP URL: `https://api.reviewbot.io/mcp`
- Transport: Streamable HTTP
- Authentication: OAuth through ReviewBot; use the client's connection flow.
- Account: an existing eligible paid or trial ReviewBot account with monitored App Store or Google Play apps.
- Server documentation: [Connection guide](https://api.reviewbot.io/mcp/docs)

In a client that supports remote OAuth MCP servers, add the URL above and complete ReviewBot authorization. Never paste passwords, access tokens, or client secrets into a conversation or this repository. Account and organization settings may control which custom connectors can be added.

### Claude

For a custom connector, add the remote MCP URL in Claude's connector settings, then complete OAuth. The connection provides the tools; the plugin package also provides the two skills below.

To inspect the local Claude Code plugin after downloading this package:

```sh
claude plugin validate /absolute/path/to/reviewbot-mcp
claude --plugin-dir /absolute/path/to/reviewbot-mcp
```

Complete connection authorization in the host before calling tools. Add the included marketplace with `/plugin marketplace add fahimk/reviewbot-mcp`, followed by `/plugin install reviewbot-app-reviews@reviewbot-app-reviews`. Complete the ReviewBot OAuth flow to connect the live endpoint.

### ChatGPT and Codex

This package uses the portable Agent Plugins format: root `plugin.json`, `mcp.json`, and `skills/`. A developer with access to custom MCP connections can add the live endpoint through ChatGPT's **Plugins → Add custom MCP server** flow and test the connection. Public directory installation becomes available only after submission, review, and publication.

OpenAI's packaging documentation adds OAuth metadata that the portable MCP 1.0.0 schema does not accept. The portable file stays schema-valid; `submission/mcp.openai.json` is the OpenAI submission variant. See [package notes](docs/package-notes.md) before uploading either archive. Custom MCP workflows have been tested in Claude and ChatGPT with synthetic data; installation of the packaged skills remains unverified. The original version 0.1.0 OpenAI archive was successfully uploaded and submitted on 2026-11-09. The listing is in review and is not publicly available.

### Cursor

Cursor supports the [Agent Plugins format](https://cursor.com/docs/plugins) used by this repository. The existing root `plugin.json`, `mcp.json`, and `skills/` provide the remote connection and both review workflows; no Cursor-specific manifest is required.

For a direct MCP connection, merge this entry into the `mcpServers` object in your existing Cursor MCP configuration. Preserve any other servers:

```json
{
  "mcpServers": {
    "reviewbot": {
      "url": "https://api.reviewbot.io/mcp"
    }
  }
}
```

Complete ReviewBot OAuth in Cursor, then ask which apps are accessible. A direct MCP connection adds tools only. To test the bundled skills as a local plugin, copy this repository's package files into `~/.cursor/plugins/local/reviewbot-app-reviews`, reload Cursor, and check **Customize** for the server and both skills. Local plugin imports must be permitted by your organization's settings. Follow Cursor's [local testing guide](https://cursor.com/docs/plugins#test-plugins-locally); a symlink pointing outside its local plugin folder is not supported.

Cursor host testing and Marketplace submission are pending. Do not interpret package compatibility as a published listing or a completed OAuth test. Maintainers can use the [Cursor and Glama submission handoff](docs/cursor-glama-submission.md).

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

Staging and production canaries passed the OAuth registration, PKCE, account consent, four-tool calls, refresh, revocation, and negative-access checks. The official MCP SDK client passed in legacy and pinned `2026-07-28` protocol modes. The unmodified Docker MCP Gateway initialized, listed the four tools, and successfully called each tool against isolated synthetic review data. That gateway test used a short-lived OAuth token; Docker CLI browser login and credential storage were not tested.

Live Claude and ChatGPT custom MCP sessions completed OAuth and exercised review statistics, search, detail, pagination, and draft-only handoff with synthetic data. Claude's initial draft incorrectly claimed an internal handoff; an explicit instruction against unconfirmed actions corrected it and passed a fresh-session check. Human review remains necessary. Both test connections were revoked afterward. Packaged skill installation remains unverified, and these checks do not establish directory approval. See [submission status](docs/submission-tracker.md) for details.

This repository contains connection metadata, skills, documentation, and a brand asset. It contains no backend source, customer review exports, or credentials. Package code and documentation are MIT licensed; ReviewBot names and artwork remain their owners' trademarks and are not licensed by MIT.

[ReviewBot](https://reviewbot.io/) · [Support](https://reviewbot.io/contact/) · [Privacy](https://reviewbot.io/privacy/) · [Terms](https://reviewbot.io/terms/)
