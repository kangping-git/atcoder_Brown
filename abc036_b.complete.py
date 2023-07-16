# B. 回転
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc036/tasks/abc036_b

import numpy as np
N = int(input())
s = []
for i in range(N):
    s.append(list(input()))
s = np.array(s)
s = np.rot90(s,k=3)
for i in range(N):
    print("".join(s[i]))

# AC
# Complete at 2023-07-15T23:46:34.969Z