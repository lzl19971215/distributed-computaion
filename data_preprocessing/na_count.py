#! /usr/bin/env python3

import sys
from operator import itemgetter

na_count = {}
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    for key, value in enumerate(items):
        count = int(value == '')
        na_count[key] = na_count.get(key, 0) + count

sorted_na_count = sorted(na_count.items(), key=itemgetter(0))
for num, count in sorted_na_count:
    print('%s\t%s' % (num, count))
