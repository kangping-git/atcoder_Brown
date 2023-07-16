# C. 浮気調査
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc010/tasks/abc010_3

import math

txa,tya,txb,tyb,T,V = map(int,input().split())
n = int(input())
flg = False
for i in range(n):
    x,y = map(int,input().split())
    if math.sqrt((x-txa) ** 2 + (y-tya) ** 2) + math.sqrt((x-txb) ** 2 + (y-tyb) ** 2) <= V * T:
        flg = True
if flg:
    print("YES")
else:
    print("NO")
    
# AC
# Complete at 2023-07-15T21:18:32.480Z