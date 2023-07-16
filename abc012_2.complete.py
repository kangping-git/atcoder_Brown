# B. 入浴時間
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc012/tasks/abc012_2

N = int(input())

h = N // 3600
m = (N // 60) % 60
s = N % 60

print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))

# AC
# Complete at 2023-07-15T21:22:24.801Z