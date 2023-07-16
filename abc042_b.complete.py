# B. Iroha Loves Strings (ABC Edition)
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc042/tasks/abc042_b
N,L = map(int,input().split())
SL = []
for i in range(N):
    S = input()
    SL.append(S)
SL.sort()
print("".join(SL))

# AC
# Complete at 2023-07-16T04:32:24.629Z