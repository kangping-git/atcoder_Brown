# B. 嘘つきの高橋くん
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc021/tasks/abc021_b

N = int(input())
a,b = map(int,input().split())
K = int(input())
P = list(map(int,input().split()))
l = set([a,b])
for i in range(K):
    if P[i] in l:
        print("NO")
        exit()
    l.add(P[i])
print("YES")

# AC
# Complete at 2023-07-15T22:03:16.169Z