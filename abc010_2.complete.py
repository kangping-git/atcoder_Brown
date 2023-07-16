# B. 花占い
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc010/tasks/abc010_2

def get(num):
    if num % 2 == 0:
        return False
    elif num % 3 == 2:
        return False
    return True

n = int(input())
a = list(map(int,input().split()))
su = 0
for i in range(n):
    m = 0
    num = a[i]
    while not get(num):
        num -= 1
        m += 1
    su += m
print(su)

# AC
# Complete at 2023-07-15T11:33:23.590Z