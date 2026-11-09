# Cursor and Glama submission handoff

Updated 2026-11-09. Cursor has not been submitted. Glama has automatically imported the official registry entry; its listing is public and searchable, with ownership verified and authenticated health checks pending. These channels use the existing hosted service and public integration package. The version 0.1.0 release and its archives remain unchanged.

## Listing fields

| Field | Value |
| --- | --- |
| Display name | ReviewBot App Reviews |
| Plugin identifier | `reviewbot-app-reviews` |
| Short description | Search collected App Store and Google Play reviews, summarize customer feedback, and draft grounded replies. |
| Homepage and setup | https://reviewbot.io/mcp/ |
| Public integration repository | https://github.com/reviewbot-io/reviewbot-mcp |
| Logo | `assets/icon.png` in the repository |
| MCP endpoint | `https://api.reviewbot.io/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth 2.0 with dynamic client registration and PKCE |
| Support | https://reviewbot.io/contact/ |
| Privacy | https://reviewbot.io/privacy/ |
| Terms | https://reviewbot.io/terms/ |
| Documentation | https://api.reviewbot.io/mcp/docs |

Suggested long description:

> Bring reviews collected for your monitored App Store and Google Play apps into your assistant. Find low-rating feedback, inspect review details, summarize recurring themes and observed rating statistics, and prepare reply drafts. Requires an eligible paid or trial ReviewBot account with monitored apps. All four tools are read-only; replies are drafts and are not published. Queries filter by collection time, cover up to 30 days, scan at most 500 records, and include coverage and freshness information. Results describe the collected sample, not every store review.

## Cursor

**Eligibility clarification pending before submission.** [Cursor's Publisher Terms](https://cursor.com/marketplace-publisher-terms), checked 2026-11-09, include MCP servers in the Plugin definition (§1.6) and prohibit direct or indirect user fees for Marketplace plugin access or use (§3.1). ReviewBot requires an eligible paid or trial account. No explicit SaaS-subscription exception was found in the official terms or plugin documentation. Obtain written clarification before accepting the publisher terms or submitting; other listed services do not establish an exception for ReviewBot. Eligibility clarification was requested on 2026-11-09. Written confirmation remains pending. Official support contact: `fahim@reviewbot.io`.

If eligibility is confirmed and host tests pass, submit the public repository URL through [Cursor's publisher form](https://cursor.com/marketplace/publish). The repository contains the root Agent Plugins manifest, canonical `mcp.json`, two skills, MIT-licensed package code/documentation, and a committed logo. The service's backend is not included in that license or repository. ReviewBot branding retains its existing license exclusion.

Follow the [official submission checklist](https://cursor.com/docs/reference/plugins#submission-checklist). The existing portable format is supported, so a second `.cursor-plugin/plugin.json` is unnecessary. The [README](../README.md#cursor) describes direct connection and local package testing.

Before claiming the package is host-tested, complete these checks in Cursor:

1. Load the package using Cursor's supported local-plugin flow; confirm both skills and exactly one ReviewBot MCP server appear.
2. Authorize an isolated synthetic ReviewBot account and confirm the four expected tools are discovered.
3. Run the weekly brief and reply-draft workflows from the installed skills. Check sample counts, collection dates, coverage limits, source references, and draft-only behavior against the [review scenarios](reviewer-scenarios.md).
4. Revoke the temporary test connection and record the tested Cursor version and outcomes. A schema check does not establish host behavior or Marketplace approval.

Cursor host testing and Marketplace submission remain pending.

## Glama

Manage the [existing ReviewBot connector](https://glama.ai/mcp/connectors/io.github.fahimk/reviewbot), imported from the official MCP Registry. It is already public and searchable. Do not create a duplicate through Add Server. The fields above are prepared for maintaining this entry; the GitHub link identifies integration metadata and documentation, not the hosted backend source.

The [official FAQ](https://glama.ai/mcp/faq#how-do-i-submit-an-mcp-connector) requires a dedicated test profile. Configure **Admin → Test Profile → OAuth 2.0** with an isolated synthetic account, no customer data, and no billable operations. Dynamic registration alone does not authorize the user. Keep credentials out of public fields, support chat, and this repository.

Health checks initialize and list metadata without invoking tools or reading resource contents. The ReviewBot entry is public; earlier health checks reported unauthorized access, and authenticated health verification remains pending. Public discoverability and successful authenticated health checks are separate states. A continuing test grant may be needed, so this is separate from a temporary demo connection.

Ownership is verified, and the endpoint proof and callback support are deployed. Live callback compatibility passes (Glama displays 'Works in Glama') and the flow reaches the synthetic ReviewBot consent screen. The dedicated synthetic OAuth test profile remains to be completed; authenticated health verification is pending. Keep account credentials and OAuth tokens out of this repository.

The public publisher profile now displays ReviewBot (Tech Labs, Inc.), with the official website and documentation, first-party relationship, paid/trial account requirement, and access-scope restrictions. The logo is uploaded and the official support contact is `fahim@reviewbot.io`.
