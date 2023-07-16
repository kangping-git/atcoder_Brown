# A. 高橋君と青木君の好きな数
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc032/tasks/abc032_a

import math
 
a = int(input())
b = int(input())
n = int(input())
 
print(math.ceil(n/(a*b//math.gcd(a,b))) * a*b//math.gcd(a,b))

# AC
# Complete at 2023-07-15T23:15:06.555Z