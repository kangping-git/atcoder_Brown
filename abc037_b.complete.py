# B. 編集
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc037/tasks/abc037_b

import numpy as np

N,Q = map(int,input().split())
l = np.zeros(N,dtype=np.int64)

for i in range(Q):
    L,R,T = map(int,input().split())
    l =np.concatenate([l[:L-1], np.full(R-L+1,T), l[R:]])
for i in range(N):
    print(l[i])

# AC
# Complete at 2023-07-15T23:57:11.392Z