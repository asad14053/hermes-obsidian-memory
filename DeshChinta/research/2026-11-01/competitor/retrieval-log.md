# Competitor retrieval log — 2026-11-01

- Channel: https://www.youtube.com/@EnayetChowdhuryOfficial/videos
- Web extraction produced a usable first-tab listing once, but a later extractor route returned only navigation text. Direct HTML with `Mozilla/5.0`, 25-second timeout, validated channel name and channel ID `UCwIzJ_UWnn1Uc8d1H8nCuUA` and recovered 30 unique `lockupViewModel` entries.
- Coverage is initial videos tab only; no continuation pages requested. Displayed relative dates are preserved as shown.
- The first video remains `YSNoS0UqGPg`, “চট্টগ্রাম বন্দর বিদেশিদের হাতে গেলে সমস্যা যেখানে”, displayed as `153K` and `2w ago`. This is metadata, not argument evidence.
- Official transcript helper was retried with `youtube-transcript-api` installed through `uv run --with`; YouTube returned an IP-block error. No cookies, account authentication, proxy relay or paid service was used.
- Exact watch-page `web_extract` failed with a keyless extractor error. A direct public watch-page fetch returned HTML but no parsable `ytInitialPlayerResponse` caption tracks. Browser escalation was blocked because the runtime's real-profile browser setting had no supported Chromium default.
- Public oEmbed validated the video title and author. The previously recovered 13,186-character transcript section remains the only content-level capture for this video; its completeness, caption authorship and timing beyond `0:00` and `4:25` remain unverified. See [[DeshChinta/research/2026-10-27-repair/competitor/competitor-recovery]].
- No newer video ID was found than the prior run, so no new competitor content argument was inferred.
