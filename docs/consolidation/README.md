# Consolidated repositories

This is the maintained project. Duplicate source and release histories are browsable inside this repository; no archive extraction is required. The active application/package files were kept identical during this history consolidation.

| Former repository | Preserved branches | Preserved release tags |
|---|---|---|
| finalSMGHedgex | [`history/finalSMGHedgex/main`](https://github.com/TanishC4444/Hedgex/tree/history/finalSMGHedgex/main) | `history/finalSMGHedgex/v1.0.0`, `history/finalSMGHedgex/v1.0.1`, `history/finalSMGHedgex/v1.0.2` |
| PCIS_FantasySMG | [`history/PCIS_FantasySMG/main`](https://github.com/TanishC4444/Hedgex/tree/history/PCIS_FantasySMG/main), [`history/PCIS_FantasySMG/shubhrose-deployment`](https://github.com/TanishC4444/Hedgex/tree/history/PCIS_FantasySMG/shubhrose-deployment) | `history/PCIS_FantasySMG/Mac` |

Every original remote branch/tag SHA is retained exactly. Original duplicate repositories are archived only after remote preservation verification. Their old URLs continue to expose their historical content.

## Additional local history

Local HedgeX source histories are also retained under `history/local-*`. The PCIS working copy contained generated executable payloads up to 234 MB that GitHub rejects. Only compiled executable/library blobs were removed from the imported copy; original local files/history were left untouched. Commit mappings record the changed IDs. No Python, JavaScript, HTML, CSS, templates, or source-data blobs were removed by that filter. Published original remote histories are retained without rewriting their IDs.

Use `git clone --filter=blob:none` for a lighter checkout that leaves historical build blobs on the server until requested.
