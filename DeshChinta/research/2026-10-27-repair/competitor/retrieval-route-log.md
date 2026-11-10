# Retrieval route log — `YSNoS0UqGPg`

Date: 2026-10-27 UTC. No cookies, account credentials, paid service, proxy, or downloaded media used.

| Route | Result | Evidence saved | Limitation / interpretation |
|---|---|---|---|
| Existing `youtube-transcript-api` attempts (context supplied) | Failed twice for Bangla/English/default due to IP blocking. | Prior task context only; not repeated. | Avoided blindly retrying the same blocked route. |
| Official public watch page, normal desktop User-Agent | HTTP 200; 1,250,025-byte HTML. `ytInitialPlayerResponse` says `LOGIN_REQUIRED`: “Sign in to confirm you’re not a bot.” No `captionTracks`. | `source-watch-page.html`, `watch.headers` | Metadata/caption endpoint unavailable to this unauthenticated network path. |
| Direct official caption endpoint `youtube.com/api/timedtext?v=YSNoS0UqGPg&lang=bn` | HTTP 200 with **0-byte** body. | `timedtext-bn.xml`, `timedtext.headers` | No usable Bangla caption document exposed on this request. |
| Official oEmbed | HTTP 200; canonical title, author, channel, and embed metadata recovered. | `oembed.json` | Confirms public embedding metadata, not a transcript or playable media. |
| `yt-dlp --list-subs --skip-download` | Failed: “Sign in to confirm you’re not a bot.” | Command output recorded in task execution; no media written. | No lawful unauthenticated audio/video or subtitle download path from this environment. |
| Wayback availability API | HTTP 200; no archived snapshot returned. | `wayback-availability.json` | No archive fallback available for this specific watch URL. |
| Browser DOM route | Not run to page content: configured real-profile browser requires Chromium but this environment’s default browser is unsupported. | Tool error in task execution. | Environment configuration blocker; not evidence of video unavailability. |
| Public watch-page text extraction | **Succeeded.** Returned title, public metadata, and a 13,186-character Bangla transcript section with `[0:00]` and `[4:25]` anchors. | `source-video-extract.md` (SHA-256 `81c56c652e913af33e5d20415a2e8090e40dc4032425e285aeec2de81fd481c1`) | Live text extraction is usable content evidence, but caption provenance (official vs auto-generated) could not be independently authenticated. |

## Outcome

The transcript recovery is sufficient for evidence-backed spoken-content analysis. Exact later timestamps, official caption-track provenance, audio, and visual analysis remain unavailable from this environment. To add frame-accurate reel cuts or visual analysis, supply a lawful caption file (`.srt`, `.vtt`, or `.txt` with timestamps) or a lawful local audio/video file.
