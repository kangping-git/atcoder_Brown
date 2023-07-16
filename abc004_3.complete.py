# C. 入れ替え
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc004/tasks/abc004_3

N = int(input()) % 30

a = list("123456")

for i in range(N):
    tmp = a[i % 5]
    a[i % 5] = a[i % 5 + 1]
    a[i % 5 + 1] = tmp
print("".join(a))

# AC
# Complete at 2023-07-15T11:10:22.911Z