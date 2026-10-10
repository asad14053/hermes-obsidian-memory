---
type: workflow
project: Bangladesh_Monitor
status: active
created: 2026-10-06
last_updated: 2026-10-06
skill: bangladesh-cross-ministry-anomaly-hunter
---

# Bangladesh Cross-Ministry Anomaly Hunter

## Skill

`bangladesh-cross-ministry-anomaly-hunter`

Use after the monthly ministry reports are complete. It reads the latest report/data/source packages across monitored ministries, finds cross-dataset anomalies, and returns at most the 10 strongest potential investigations. It does not produce a ministry-by-ministry summary.

It inherits the evidence, bilingual-search, media-classification, article-record, citation and non-accusation standards established by `bangladesh-ministry-data-watch`.

## Output paths

- `Bangladesh_Monitor/cross-ministry-anomaly-hunter/reports/YYYY-MM.md`
- `Bangladesh_Monitor/cross-ministry-anomaly-hunter/data/YYYY-MM.csv`
- `Bangladesh_Monitor/cross-ministry-anomaly-hunter/candidates/YYYY-MM.json`
- `Bangladesh_Monitor/cross-ministry-anomaly-hunter/sources/YYYY-MM.json`
- `Bangladesh_Monitor/cross-ministry-anomaly-hunter/sources/YYYY-MM-articles.json`
- `Bangladesh_Monitor/cross-ministry-anomaly-hunter/figures/YYYY-MM/`

## Cron prompt

> Load `bangladesh-cross-ministry-anomaly-hunter` and `bangladesh-ministry-data-watch`. Read the latest completed monthly report, data and source packages for every monitored Bangladesh ministry. Do not summarize ministries. Find cross-ministry anomalies, apply the evidence and legal-risk gates, recompute scores with the skill validator, and save only the strongest 10 qualifying investigations under `Bangladesh_Monitor/cross-ministry-anomaly-hunter/` for the reporting month. Never pad the list or treat an anomaly as proof of wrongdoing.
