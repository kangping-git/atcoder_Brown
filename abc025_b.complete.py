# B. 双子とスイカ割り
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc025/tasks/abc025_b

N,A,B = map(int,input().split())
t = 0
for i in range(N):
    s,d = input().split()
    d = int(d)
    if d < A:
        d = A
    elif d > B:
        d = B
    if s == "East":
        t += d
    else:
        t -= d
if t > 0:
    print("East",t)
elif t == 0:
    print(0)
else:
    print("West",-t)

# AC
# Complete at 2023-07-15T22:48:51.308Z