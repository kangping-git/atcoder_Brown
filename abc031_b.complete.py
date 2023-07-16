# B. 運動管理
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc031/tasks/abc031_b

L,H = map(int,input().split())
N = int(input())
for i in range(N):
    A = int(input())
    if A < L:
        print(L-A)
    elif A <= H:
        print(0)
    else:
        print(-1)
# AC
# Complete at 2023-07-15T23:14:51.967Z