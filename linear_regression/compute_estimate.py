#! /usr/bin/python3
import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--p_num", help="the number of variables", type=int)
args = parser.parse_args()
matrix = []
for line in sys.stdin:
    line = line.strip()
    spl = line.split('\t')
    index, value = int(spl[0]), spl[1:]
    if index < args.p_num:
        matrix.append(value)
    else:
        xty = np.array(value, dtype=float).reshape(-1, 1)
matrix = np.array(matrix, dtype=float)
inverse = np.linalg.pinv(matrix)
beta = np.squeeze(np.dot(inverse, xty))
print(' '.join(str(e) for e in beta))





