#! /usr/bin/python3
import sys
import numpy as np

X = []
Y = []
for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    x = line[:-1]
    y = line[-1]
    X.append(x)
    Y.append(y)
X = np.array(X, dtype=float)
Y = np.array(Y, dtype=float).reshape(-1, 1)
beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
print(beta)
