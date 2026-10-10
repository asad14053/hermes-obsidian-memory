---
type: source-policy
project: Bangladesh_Monitor
status: canonical
created: 2026-10-06
last_updated: 2026-10-06
---

# Bangladesh News & Media Source Policy

## Core rule

News media are **secondary evidence**. Government datasets, official documents, audit reports, court records, procurement records and original statistics remain primary.

For every major finding seek:

- **Primary source + independent Bangladesh media**, or
- for major/high-risk claims, **primary + two genuinely independent media sources**, or
- **primary + Bangladesh media + international/NGO/research evidence**.

Never count syndication or repeated government releases as independent corroboration.

## Preferred Bangladesh outlets

### High-priority general reporting

- Prothom Alo / প্রথম আলো — `prothomalo.com`, `en.prothomalo.com`
- The Daily Star — `thedailystar.net`
- bdnews24.com — `bdnews24.com`
- Dhaka Tribune — `dhakatribune.com`
- New Age — `newagebd.net`

### Business, economic and infrastructure

- The Business Standard — `tbsnews.net`
- The Financial Express — `thefinancialexpress.com.bd`
- Bonik Barta / বণিক বার্তা — `bonikbarta.com`

Prioritize these for finance, planning, commerce, power/energy, industries, agriculture, food, shipping, roads, Bangladesh Bank, NBR, trade, inflation, banking, energy and government projects.

### Additional national reporting

Ittefaq, Samakal, Jugantor, Kaler Kantho, Bangla Tribune and Jago News 24 are useful for district events, Bengali documents, local complaints, ministry statements and triangulation.

## Television and broadcast

Preferred: Jamuna TV, Somoy TV, Channel 24, Independent Television, Ekattor TV, DBC News, ATN News, News24, Ekhon TV, NTV and Channel i.

Use broadcast reporting for breaking events, field reporting, interviews, video evidence, minister statements, disasters, protests, accidents and public reaction. A television headline alone never proves a numerical claim; locate the underlying report or official dataset.

## Government-owned and official news

Classify BSS, BTV, PID, ministry press releases and agency releases as **OFFICIAL GOVERNMENT POSITION**, not independent verification.

If a ministry makes a claim and BSS repeats it, that is one official claim—not two sources. Test it against relevant data and genuinely independent reporting.

## International cross-checks

For major national stories search Reuters, Associated Press, BBC/BBC Bangla, AFP, Al Jazeera, Deutsche Welle/DW Bangla, Financial Times, Nikkei Asia and The Economist when relevant. Reuters/AP receive high weight for straightforward factual confirmation, while the underlying primary record remains preferable.

## Cross-outlet and originality rule

Identify the original source of each claim. Newspaper copies of BSS, another newspaper repeating the same copy and television repetition of the same release constitute one underlying source. Do not count copied or syndicated versions as independent corroboration.

## Bilingual search

Search every material topic in English and Bangla. Translate the ministry name, metric and investigative concepts.

Examples:

- `Ministry of Food rice stock September 2026`
- `খাদ্য মন্ত্রণালয় চালের মজুত সেপ্টেম্বর ২০২৬`
- `Bangladesh road accident September 2026`
- `সড়ক দুর্ঘটনা সেপ্টেম্বর ২০২৬`
- `ADP implementation September 2026`
- `এডিপি বাস্তবায়ন সেপ্টেম্বর ২০২৬`

## Investigative search patterns

Combine ministry and agency names with:

**English:** investigation, irregularity, corruption, audit, project delay, cost overrun, tender, procurement, contract, allegation, complaint, shortage, failure, death, accident, protest, strike, lawsuit, court, investigation committee, inquiry, data discrepancy, revised estimate.

**Bangla:** অনিয়ম, দুর্নীতি, অডিট, প্রকল্প বিলম্ব, ব্যয় বৃদ্ধি, দরপত্র, ক্রয়, অভিযোগ, সংকট, ঘাটতি, ব্যর্থতা, দুর্ঘটনা, মৃত্যু, বিক্ষোভ, মামলা, তদন্ত, তদন্ত কমিটি, হিসাব, তথ্যের গরমিল, ব্যয়, বরাদ্দ.

Never infer guilt because these terms appear. Trace allegations to original records, named evidence and the relevant institution's response.

## Story-triangulation template

**OFFICIAL VERSION:** What does the ministry/government say?  
**DATA:** What do primary statistics/documents show?  
**MEDIA REPORTING:** What have independent journalists found?  
**EXPERT/NGO POSITION:** What do credible researchers/watchdogs say?  
**CONFLICT:** Where do the sources agree or diverge?

## Article-level reliability test

Do not assign permanent outlet truth scores. Evaluate each item:

1. Named reporter?
2. Clear publication date?
3. Direct documents linked?
4. Named sources?
5. Multiple independent sources?
6. Precise data cited?
7. Response from the relevant institution?
8. Original reporting or copied material?
9. Correction/update history?
10. Headline supported by the article?

Prefer original investigative reporting over opinion columns or talk-show commentary for major claims.

## Required saved-article record

Every retained article must have one structured record containing:

- `outlet`
- `headline`
- `author`
- `publication_datetime`
- `URL`
- `article_type`
- `original_reporting` = `yes`, `no` or `unclear`
- `government_source` = `yes` or `no`
- `primary_document_linked` = `yes` or `no`
- `key_claim`
- `data_numbers`
- `people_quoted`
- `underlying_source`
- `corroborated_by`
- `confidence` = `high`, `medium` or `low`

`data_numbers`, `people_quoted`, `underlying_source` and `corroborated_by` are arrays. Use `null` for undisclosed scalar metadata and an empty array where the article discloses no items. Never invent a byline, publication time, quoted person, document link, underlying source or corroborator. Confidence applies to the article/claim record, not permanently to the outlet.

## Lead-only sources

Anonymous Facebook posts, random Facebook pages, TikTok, YouTube commentary, unsourced X/Twitter posts, aggregators, copied articles, screenshots without originals, partisan memes and anonymous blogs may generate leads only. They cannot establish facts without independent verification.
