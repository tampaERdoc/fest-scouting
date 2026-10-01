# Festival Scouting

Password-protected static site for scouting festival lineups: audience (Instagram/Spotify), label and booking data, plus a graded support-slot target cohort.

The data files are encrypted (AES-256-GCM, key derived from the password with PBKDF2-SHA256, 310k iterations). The page decrypts them in the browser after the password is entered, so this repository and the published site contain no readable band data. The page is also marked `noindex` so search engines don't list it.

## Festivals
| Toggle | Encrypted data file | Status |
|---|---|---|
| Warped Tour 2026 (Orlando, Nov 14–15) | `data/warped-2026.enc.js` | Live — 143 acts, compiled Oct 1, 2026 |
| Fest 2026 | `data/fest-2026.enc.js` | Coming soon |

## Adding a festival
1. Put the plaintext dataset at `private/<id>.json` (same shape as the Warped file; `private/` is git-ignored and never pushed).
2. Run `python3 tools/encrypt.py <id> "<the same password>"` — writes `data/<id>.enc.js`.
3. Make sure `{id:'<id>', label:'…'}` is in `FEST_REGISTRY` in `index.html` (Fest 2026 is already listed).
4. Commit and push `data/<id>.enc.js`.

## Changing the password
Re-run step 2 for every festival with the new password and push.
