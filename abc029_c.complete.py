# C. Brute-force Attack
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc029/tasks/abc029_c

import numpy as np

N = int(input())
for i in range(3 ** N):
    b = list(np.base_repr(i,3).zfill(N))
    s = ""
    for i in range(N):
        if b[i] == "0":
            s += "a"
        elif b[i] == "1":
            s += "b"
        else:
            s += "c"
    print(s)

# AC
# Complete at 2023-07-15T23:04:43.331Z