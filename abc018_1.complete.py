# A. 豆まき
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc018/tasks/abc018_1

A = int(input())
B = int(input())
C = int(input())
 
_A = sorted([A,B,C],reverse=True)
 
print(_A.index(A)+1)
print(_A.index(B)+1)
print(_A.index(C)+1)

# AC
# Complete at 2023-07-15T21:48:45.082Z