# Festival Scouting

Password-protected static site for scouting festival lineups: audience (Instagram/Spotify), label and booking data, plus a graded support-slot target cohort benchmarked against Sincere Engineer.

Data files are encrypted (AES-256-GCM, key derived with PBKDF2-SHA256, 310k iterations) and decrypted in the browser after the password is entered, so neither this repository nor the published site exposes readable band data. The page is `noindex` so search engines don't list it.

## Festivals
| Toggle | Encrypted data file | Acts |
|---|---|---|
| Warped Tour 2026 (Orlando, Nov 14–15) | `data/warped-2026.enc.js` | 143 |
| Fest 2026 / FEST 24 (Gainesville, Oct 23–25) | `data/fest-2026.enc.js` | 334 |
| All Festivals | *(virtual — merges every loaded festival)* | 477 |

The **All Festivals** toggle appears automatically once two or more festivals are present. It adds a Festival column and filter so you can, for example, list every A+ band across both bills or every band on one label.

## Adding a festival
1. Put the plaintext dataset at `private/<id>.json` — same shape as the existing ones:
   `{label, title, kicker, subtitle, cohortLede, generated, benchmark, examples[], notes, bands[]}`.
   Each band: `name, grade, pitch, genre, day, hometown, status, instagram_handle, instagram_followers,
   instagram_source, instagram_url, spotify_listeners, spotify_url, size_vs_sincere_engineer, label, label_note,
   label_source, agency, agent, booking_notes, booking_evidence, booking_source, flags`.
   (`private/` is git-ignored and never pushed.)
2. `python3 tools/encrypt.py <id> "<the same password>"` → writes `data/<id>.enc.js`.
3. Add `{id:'<id>', label:'…'}` to `FEST_REGISTRY` near the bottom of `index.html`.
4. Commit and push `data/<id>.enc.js`.

Booking-agency filter options are derived from the data, so new agencies appear on their own.

## Changing the password
Re-run step 2 for every festival with the new password, then push.
