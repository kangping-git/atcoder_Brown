# A. Iroha and Haiku (ABC Edition)
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc042/tasks/abc042_a

A = list(map(int,input().split()))
if A.count(7) == 1 and A.count(5) == 2:
    print("YES")
else:
    print("NO")

# AC
# Complete at 2023-07-16T04:30:34.002Z