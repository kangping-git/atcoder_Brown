# B. N重丸
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc026/tasks/abc026_b

N = int(input())
R = []
for i in range(N):
    R.append(int(input()))
R.sort(reverse=True)
S = 0
for i in range(N):
    if i % 2 == 0:
        S += R[i] ** 2
    else:
        S -= R[i] ** 2
print(S * 3.141592653589793238)

# AC
# Complete at 2023-07-15T22:51:32.134Z