# A. 動物園
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc024/tasks/abc024_a

A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
 
M = (S+T) >= K
 
if M:
    print((A-C)*S + (B-C)*T)
else:
    print(A*S + B*T)

# AC
# Complete at 2023-07-15T22:25:58.586Z