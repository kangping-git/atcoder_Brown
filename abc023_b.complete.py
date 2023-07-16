# B. 手芸王
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc023/tasks/abc023_b
def accessory(N,s):
    if N == 0:
        return "b"
    if N % 3 == 1:
        return "a" + s + "c"
    if N % 3 == 2:
        return "c" + s + "a"
    if N % 3 == 0:
        return "b" + s + "b"
N = int(input())
S = input()
N = 0
s = ""
while len(s) < len(S):
    s = accessory(N,s)
    N += 1
if s == S:
    print(N-1)
else:
    print(-1)
# AC
# Complete at 2023-07-15T22:25:14.565Z