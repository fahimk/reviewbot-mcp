# Submission tracker

Updated 2026-11-04. The production service is live. Status below distinguishes published registry metadata, submitted listings, and attempts blocked before upload. Directory approval is not implied by a validator or interoperability test.

| Channel | Status | Evidence | Next step |
| --- | --- | --- | --- |
| Public package repository | **Published — v0.1.0** | [Release and archives](https://github.com/fahimk/reviewbot-mcp/releases/tag/v0.1.0) | Maintain release metadata and future versions. This repository contains integration metadata, skills, and docs; no hosted backend source. |
| Official MCP Registry | **Active — 0.1.0** | [Published record](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.fahimk%2Freviewbot/versions/0.1.0), published 2026-11-04 | Keep metadata aligned with future server releases. |
| Claude plugin directory | **Submitted — In Review** | [Submission portal](https://claude.ai/directory/manage/plugins/d6c5d38b-f5fe-41d6-ae4c-d6fad861a586) | Security scan passed with directory-policy warnings. A human reviewer is checking the submission; the requested publisher name, ReviewBot, also awaits human review. Submitted version 0.1.0 references commit `454fb1f`. The listing is not live, and no separate MCP connector approval is recorded here. |
| Docker MCP catalog | **PR open — maintainer action required** | [docker/mcp-registry#6604](https://github.com/docker/mcp-registry/pull/6604) | Maintainers must approve fork CI execution and review the contribution. CI and security-review workflows are gated; no upstream jobs have run. The listing is not accepted or merged. |
| OpenAI shared ChatGPT/Codex directory | **Identity verified — upload blocked by portal error** | On 2026-11-04, identity showed Verified in the signed-in [developer dashboard](https://platform.openai.com/plugins). Three upload attempts, including a fresh page load, returned `Invalid URL`. | Resolve the portal upload error, then upload the prepared archive and run its scan/review. No successful upload, scan, or directory submission has occurred. |
| Glama | Not submitted | [MCP directory](https://glama.ai/mcp/servers) → Add Server | Obtain account access and confirm eligibility for a hosted service with a thin public integration package. Do not describe the hosted backend as open source. |
| PulseMCP | Submissions paused | [Submission page](https://www.pulsemcp.com/submit) | The directory says it will automatically ingest official MCP Registry entries when submissions resume. No separate ReviewBot submission was made. |
| MCP.so | Paid route skipped | [Server submission](https://mcp.so/submit?type=server) | The observed submission route costs $39. No free route was observed and no payment was authorized or made. |
| Smithery | Not submitted; no straightforward free route verified | [Platform update](https://smithery.ai/future) | Following the proxy, account, API, and CLI shutdown, a curated directory remains. Recheck for a suitable free submission route; no ReviewBot submission was made. |

## Verification evidence

- The [ReviewBot MCP setup and workflow page](https://reviewbot.io/mcp/), production MCP endpoint, and [connection documentation](https://api.reviewbot.io/mcp/docs) are live. Backend, dashboard, and landing-page production rollouts completed.
- Staging and production canaries passed dynamic client registration, PKCE, browser-cookie-bound Firebase account consent, scoped tool calls, refresh, revocation, and negative access cases.
- The official MCP SDK client passed in legacy and pinned `2026-07-28` modes. Tests cover all four read-only tools and bounded inputs.
- The unmodified official Docker MCP Gateway passed six checks: initialization, listing exactly the four supported tools, and one successful call to each tool. It used an isolated synthetic reviewer account and a short-lived OAuth token; the dedicated test connection was revoked afterward. Docker CLI browser login and credential storage were not tested.
- Portable manifests, the registry entry, both skills, local Claude package validation, and archive integrity checks passed. These results do not replace directory review.
- Actual Claude and ChatGPT tool/skill sessions remain unverified. Claude's security scan passed and the submission is in human review; neither establishes end-user host compatibility.
- A dedicated non-admin reviewer account contains isolated synthetic sample data. Its credentials are kept outside this repository and all release archives.
- OpenAI developer identity is verified. Portal scan and reviewer demo/access review remain pending because the upload flow returns `Invalid URL`.

## Metadata and distribution

The official registry hosts discovery metadata for `io.github.fahimk/reviewbot`; it does not host the service or manage payments. The remote URL uses Streamable HTTP and ReviewBot OAuth. There is no npm runtime package or new billing integration.

The package identifier is `reviewbot-app-reviews`, with display name **ReviewBot App Reviews**. Both skills use the same four read-only tools: `list_apps`, `search_reviews`, `get_review`, and `get_review_stats`. Queries cover collected App Store and Google Play reviews, with a maximum 30-day collection window, at most 50 results per search page, and a 500-record scan bound per query. Reply workflows produce drafts only.

No paid directory placement has been purchased. No reviewer password, token, customer export, or private deployment artifact is included in this package.

## Submission references

- [Claude plugin submission](https://claude.com/docs/plugins/submit): validation, review, and publication are separate steps.
- [OpenAI submission](https://developers.openai.com/plugins/deploy/submission): identity verification and MCP review materials are required before publication.
- [OpenAI packaging](https://developers.openai.com/plugins/build/plugins): portable manifests and the documented OAuth extension.
- [Official MCP remote entries](https://modelcontextprotocol.io/registry/remote-servers): registry metadata for hosted servers.
