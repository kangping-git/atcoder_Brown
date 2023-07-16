# B. 文字列の反転
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc018/tasks/abc018_2

S = input()
N = int(input())
for i in range(N):
    l,r = map(int,input().split())
    S = S[:l-1] + S[l-1:r][::-1] + S[r:]
print(S)

# AC
# Complete at 2023-07-15T21:52:05.430Z