# A. Best Body
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc022/tasks/abc022_a

best = []
 
N,S,T = map(int,input().split())
W = int(input())
if S <= W and W <= T:
    best.append(str(1))
for i in range(N-1):
    W += int(input())
    if S <= W and W <= T:
        best.append(str(i + 2))
print(len(best))

# AC
# Complete at 2023-07-15T22:03:35.718Z