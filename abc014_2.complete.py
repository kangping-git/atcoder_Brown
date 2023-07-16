# B. 価格の合計
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc014/tasks/abc014_2

n,X = map(int,input().split())
a = list(map(int,input().split()))

v = 1

su = 0
for i in range(n):
    if X & v != 0:
        su += a[i]
    v *= 2
print(su)

# AC
# Complete at 2023-07-15T21:35:25.819Z