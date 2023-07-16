# B. 心配性な富豪、ファミリーレストランに行く。
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc009/tasks/abc009_2

N = int(input())
A = set([])
for i in range(N):
    A.add(int(input()))
A = list(A)
A.sort(reverse=True)
print(A[1])

# AC
# Complete at 2023-07-15T11:22:16.480Z