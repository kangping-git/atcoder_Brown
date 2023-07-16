# B. A±B Problem
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc016/tasks/abc016_2

A,B,C = map(int,input().split())
A_plus_B = A+B
A_sub_B = A-B

if A_plus_B == C and A_sub_B == C:
    print("?")
elif A_plus_B == C:
    print("+")
elif A_sub_B == C:
    print("-")
else:
    print("!")

# AC
# Complete at 2023-07-15T21:39:30.649Z