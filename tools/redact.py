#!/usr/bin/env python3
"""Enforce the removals the datasets must carry, whatever a rebuild regenerates.

Builders regenerate the band arrays from source data, so anything deliberately
taken out has to be re-applied here. Run this after any rebuild and before
encrypting. tools/copy.py calls it, so running that is enough.
"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Earnings estimates that must never be published, by band name.
NO_EARNINGS = {
    'Sulynn Hago': 'Earnings estimate removed at the band’s request — not published.',
}
NUM = ['earnings_rank', 'est_income_top_member', 'est_income_members_sum']
TXT = ['earnings_confidence', 'earnings_error_band', 'earnings_caveat', 'earnings_source']

def redact(path):
    d = json.load(open(path, encoding='utf-8'))
    hits = 0
    for b in d.get('bands', []):
        note = NO_EARNINGS.get(b.get('name'))
        if not note:
            continue
        if any(b.get(k) not in (None, '', []) for k in NUM + TXT + ['earnings_members']):
            hits += 1
        for k in NUM: b[k] = None
        for k in TXT: b[k] = ''
        b['earnings_members'] = []
        if note not in (b.get('flags') or ''):
            b['flags'] = ((b.get('flags') or '') + ' ' + note).strip()
    if hits:
        json.dump(d, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    return hits

if __name__ == '__main__':
    total = 0
    for fid in ('warped-2026', 'riot-2026', 'fest-2026', 'watchlist-2026'):
        p = os.path.join(root, 'private', fid + '.json')
        if not os.path.exists(p): continue
        n = redact(p)
        total += n
        print('%-16s %s' % (fid, 'redacted %d record(s)' % n if n else 'already clean'))
    print('done' if not total else 're-encrypt the affected datasets')
