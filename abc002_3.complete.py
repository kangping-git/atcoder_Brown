# C. 直訴
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc002/tasks/abc002_3

import math

x_a,y_a,x_b,y_b,x_c,y_c = map(int,input().split())

a = math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
b = math.sqrt((x_c - x_b) ** 2 + (y_c - y_b) ** 2)
c = math.sqrt((x_a - x_c) ** 2 + (y_a - y_c) ** 2)

s = (a+b+c) / 2

print(math.sqrt(s * (s-a) * (s-b) * (s-c)))

# AC
# Complete at 2023-07-08T10:24:16.473Z