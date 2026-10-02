#!/usr/bin/env python3
"""Apply the site's written copy to every dataset.

Re-run this after any rebuild of private/*.json — the builders regenerate the
band arrays and would otherwise drop these fields.
"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDE = ("A+ means the band draws about the room Sincere Engineer draws and plays something close "
        "to what Sulynn plays. Starred bands were picked by hand, with a written reason. "
        "Click any band for its full record.")
COPY = {
 'warped-2026': dict(
   headline='Who could we open for on Warped?',
   where='<b>Vans Warped Tour 2026</b> — Camping World Stadium Campus, Orlando, 14–15 November. 143 acts on the bill.',
   subtitle="143 acts, each placed against Sincere Engineer's draw and ranked by how close its music sits to Sulynn's."),
 'riot-2026': dict(
   headline='Who could we open for at Riot Fest?',
   where='<b>Riot Fest 2026</b> — Douglass Park, Chicago, 18–20 September. 106 acts, Sincere Engineer among them on the Sunday.',
   subtitle="106 acts, each placed against Sincere Engineer's draw. She played this bill herself, which makes it the truest read of the three."),
 'fest-2026': dict(
   headline='Who could we open for at Fest?',
   where='<b>The Fest 24</b> — downtown Gainesville, 23–25 October. 334 acts; day and venue assignments not published yet.',
   subtitle="334 acts, each placed against Sincere Engineer's draw and ranked by how close its music sits to Sulynn's."),
 'watchlist-2026': dict(
   headline='Who else should we be watching?',
   where='<b>Follow list</b> — 746 bands drawn from the punk and indie earnings ranking. Not on any 2026 bill we track, but worth knowing.',
   subtitle="746 bands, each placed against Sincere Engineer's draw. Earnings here are modelled estimates, not reported figures."),
}
for fid, c in COPY.items():
    p = os.path.join(root, 'private', fid + '.json')
    d = json.load(open(p, encoding='utf-8'))
    d.update(c); d['cohortLede'] = LEDE
    json.dump(d, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('copy applied to', fid)
