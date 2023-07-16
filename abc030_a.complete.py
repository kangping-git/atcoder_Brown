# A. 勝率計算
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc030/tasks/abc030_a

from fractions import Fraction
 
A,B,C,D = map(int,input().split())
 
A_B = Fraction(B,A)
C_D = Fraction(D,C)
 
if A_B > C_D:
    print("TAKAHASHI")
elif A_B < C_D:
    print("AOKI")
else:
    print("DRAW")

# AC
# Complete at 2023-07-15T23:05:44.050Z