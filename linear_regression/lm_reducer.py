#! /usr/bin/env/python3


import sys
import numpy as np
from operator import itemgetter
dic = {}
for line in sys.stdin:
    line = line.strip()
    row = line.split('\t')
    index, value = int(row[0]), np.array(row[1:], dtype=float)
    dic[index] = dic.get(index, np.zeros_like(value)) + value

sorted_dic = sorted(dic.items(), key=itemgetter(0))
for index, value in sorted_dic:
    print('{}\t{}'.format(index, '\t'.join(str(e) for e in value)))
