# B. Painting Balls with AtCoDeer
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc046/tasks/abc046_b

N,K = map(int,input().split())
print(K * (K-1) ** (N-1))

# AC
# Complete at 2023-07-16T05:20:24.805Z