# B. 回転
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc004/tasks/abc004_2

import numpy as np

c = []
for i in range(4):
    c.append(input().split())

a = np.array(c)
a = np.rot90(a)
a = np.rot90(a)

for i in range(4):
    print(*a[i])

# AC
# Complete at 2023-07-15T10:33:54.719Z