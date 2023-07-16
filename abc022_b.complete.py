# B. Bumble Bee
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc022/tasks/abc022_b

N = int(input())
access = set()
already = []
for i in range(N):
    A = int(input())
    if A in access:
        already.append(A)
    access.add(A)
print(len(already))

# AC
# Complete at 2023-07-15T22:18:29.486Z