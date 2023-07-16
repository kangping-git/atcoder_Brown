# B. 自動ドア
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc024/tasks/abc024_b

N,T = map(int,input().split())
A = []
for i in range(N):
    A.append(int(input()))

t = 0
for i in range(1,N):
    if i == N:
        t += T
        continue
    if A[i] - A[i-1] >= T:
        t += T
    else:
        t += A[i] - A[i-1]
print(t+T)

# AC
# Complete at 2023-07-15T22:42:23.911Z