# B. 高橋くんの集計
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc015/tasks/abc015_2

import math

N = int(input())
A = list(map(int,input().split()))
count = 0

for i in range(N):
    if A[i] >= 1:
        count += 1

print(math.ceil(sum(A) / count))

# AC
# Complete at 2023-07-15T21:37:02.832Z