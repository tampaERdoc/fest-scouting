#!/usr/bin/env python3
"""Encrypt a festival dataset for the password-protected site.

Usage:  python3 tools/encrypt.py <fest-id> "<password>"
Reads   private/<fest-id>.json   (plaintext, never committed — private/ is git-ignored)
Writes  data/<fest-id>.enc.js    (AES-256-GCM, key from PBKDF2-SHA256)
Use the SAME password for every festival so one unlock opens them all.
"""
import sys, os, json, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
ITER = 310000
fid, pw = sys.argv[1], sys.argv[2]
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plain = open(os.path.join(root, 'private', fid + '.json'), 'rb').read()
json.loads(plain)  # validate
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pw.encode())
ct = AESGCM(key).encrypt(iv, plain, None)
b = lambda x: base64.b64encode(x).decode()
out = {"v": 1, "iter": ITER, "salt": b(salt), "iv": b(iv), "ct": b(ct)}
with open(os.path.join(root, 'data', fid + '.enc.js'), 'w') as f:
    f.write('(window.FESTS_ENC=window.FESTS_ENC||{})[%s]=%s;\n' % (json.dumps(fid), json.dumps(out)))
print('wrote data/%s.enc.js (%d bytes plaintext)' % (fid, len(plain)))
