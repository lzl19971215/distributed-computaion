#! /usr/bin/env/python3


import sys
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--y_index", default=-1, help="the column index of label y", type=int)
args = parser.parse_args()
for line in sys.stdin:
    line = line.strip()
    row = line.split('\t')
    p = len(row) - 1
    y = float(row[args.y_index])
    row.pop(args.y_index)
    x = np.array(row, dtype='float').reshape(-1, p)

    xtx = np.dot(x.T, x)
    xty = np.squeeze(x * y)
    for i in range(p):
        print('{}\t{}'.format(i, '\t'.join(str(e) for e in xtx[i])))
    print('{}\t{}'.format(p, '\t'.join(str(e) for e in xty)))

