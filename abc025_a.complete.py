# A. 25個の文字列
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc025/tasks/abc025_a

S = sorted(list(input()))
N = int(input())
 
Ses = []
 
for x in range(len(S)):
    for y in range(len(S)):
        Ses.append(S[x] + S[y])
 
print(Ses[N-1])

# AC
# Complete at 2023-07-15T22:43:00.849Z