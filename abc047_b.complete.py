# B. Snuke's Coloring 2 (ABC Edit)
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc047/tasks/abc047_b
W,H,N = map(int,input().split())
l,r,t,b = 0,W,0,H
for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        l = max(l,x)
    elif a == 2:
        r = min(r,x)
    elif a == 3:
        t = max(t,y)
    else:
        b = min(b,y)
if r - l > 0 and b - t > 0:
    print((r-l) * (b-t))
else:
    print(0)

# AC
# Complete at 2023-07-16T05:34:54.553Z