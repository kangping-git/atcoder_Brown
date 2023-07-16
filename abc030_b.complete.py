# B. 時計盤
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc030/tasks/abc030_b

n,m = map(int,input().split())
n += m/60
print(min(abs((m * 6 - n*30) % 360),abs(360 - (m * 6 - n*30) % 360)))

# AC
# Complete at 2023-07-15T23:09:13.870Z