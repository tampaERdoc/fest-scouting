# Band Scouting

Password-protected static site for scouting bands: audience (Instagram/Spotify), label, booking and modeled-earnings data, plus a graded support-slot target cohort benchmarked against Sincere Engineer.

Data files are encrypted (AES-256-GCM, key derived with PBKDF2-SHA256, 310k iterations) and decrypted in the browser after the password is entered, so neither this repository nor the published site exposes readable band data. The page is `noindex` so search engines don't list it.

## Datasets
| Toggle | Encrypted data file | Acts |
|---|---|---|
| Warped Tour 2026 (Orlando, Nov 14–15) | `data/warped-2026.enc.js` | 143 |
| Fest 2026 / FEST 24 (Gainesville, Oct 23–25) | `data/fest-2026.enc.js` | 334 |
| Watchlist (bands to follow, not on either bill) | `data/watchlist-2026.enc.js` | 746 |
| All Bands | *(virtual — merges every loaded dataset)* | 1,223 |

The **All Bands** toggle appears automatically once two or more datasets are present. It adds a "Source list" column and filter, so you can list every A+ band across all three lists, or every band on one label.

`#warped-2026`, `#fest-2026`, `#watchlist-2026` and `#all` are deep-linkable.

## Estimated earnings
The earnings columns come from a supplied punk/indie earnings ranking workbook and are **modeled estimates, not reported or audited figures**. The source derives each from touring tier, venue capacity, catalog ownership, songwriting splits and label structure, and states error bars of ±40% for ranks 1–300 and ±60% for 301–803; ranks 804–1000 are "cohort positions" describing a place in the scene economy rather than a real individual. The workbook ranks **people**, not bands, so a band may contribute several rows: `est_income_top_member` is the highest single estimate and `est_income_members_sum` adds only the members the workbook lists. Every detail view carries the caveat and the per-member breakdown; the table column is asterisked.

## Adding a dataset
1. Put the plaintext dataset at `private/<id>.json` — same shape as the existing ones:
   `{label, title, kicker, subtitle, cohortLede, generated, benchmark, examples[], notes, bands[]}`.
   Each band:
   `name, entity_type, grade, pitch, genre, genre_source, day, hometown, status, instagram_handle,
   instagram_followers, instagram_source, ig_socialblade, ig_hypeauditor, ig_hypeauditor_date, instagram_url,
   spotify_listeners, spotify_followers, spotify_url, spotify_name, spotify_verification,
   size_vs_sincere_engineer, label, label_note, label_source, agency, agent, booking_notes, booking_evidence,
   booking_source, flags, earnings_rank, est_income_top_member, est_income_members_sum, earnings_confidence,
   earnings_error_band, earnings_members[], earnings_caveat, earnings_source, follower_source_date, watchlist`
   Numeric fields must be `null` (not `""`) when unknown, or range filters will treat them as zero.
   (`private/` is git-ignored and never pushed.)
2. `python3 tools/encrypt.py <id> "<the same password>"` → writes `data/<id>.enc.js`.
3. Add `{id:'<id>', label:'…'}` to `FEST_REGISTRY` near the top of the script in `index.html`.
4. Commit and push `data/<id>.enc.js`.

Filter options are derived from the data, so new labels, agencies, genres and record types appear on their own. Any filter with more than 25 options renders as a type-to-search box instead of a dropdown.

## Changing the password
Re-run step 2 for every dataset with the new password, then push.
