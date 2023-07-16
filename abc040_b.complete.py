# B. □□□□□
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc040/tasks/abc040_b

N = int(input())
m = 99999999999999999999999999
for h in range(1,N+1):
    w = N//h
    s = N - h*w
    m = min(m,s+abs(w-h))
print(m)

# AC
# Complete at 2023-07-16T03:49:53.885Z