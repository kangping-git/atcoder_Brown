# A. Tak and Hotels (ABC Edit)
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc044/tasks/abc044_a

N = int(input())
K = int(input())
X = int(input())
Y = int(input())

s = 0
for i in range(N):
    if i < K:
        s += X
    else:
        s += Y
print(s)

# AC
# Complete at 2023-07-16T04:39:08.110Z