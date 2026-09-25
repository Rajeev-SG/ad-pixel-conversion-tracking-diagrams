#!/usr/bin/env python3
"""Fail if any image referenced from README.md is missing from the repo.

This repo's whole value is 'every diagram and screenshot visible in the README',
so broken image links are the one failure mode worth a CI gate.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, 'README.md')

with open(README, encoding='utf-8') as f:
    text = f.read()

# markdown images ![alt](path) and inline HTML <img src="path">
paths = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
paths += re.findall(r'<img[^>]+src="([^"]+)"', text)

missing, checked = [], 0
for p in paths:
    if p.startswith(('http://', 'https://', 'data:')):
        continue
    checked += 1
    rel = p.split('#')[0].split('?')[0]
    if not os.path.exists(os.path.join(ROOT, rel)):
        missing.append(rel)

print(f'Checked {checked} local image references in README.md')
if missing:
    print('MISSING image files:')
    for m in sorted(set(missing)):
        print('  -', m)
    sys.exit(1)
print('All referenced images exist.')
