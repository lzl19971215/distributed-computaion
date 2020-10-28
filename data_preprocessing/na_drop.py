#! /usr/bin/env python3

import sys


for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    if len(items) != 57:
        continue
    have_na = False
    for item in items:
        if item == '':
            have_na = True
            break
    if not have_na:
        print('\t'.join([str(item) for item in items]))
