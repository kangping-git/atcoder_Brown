# C. 九九足し算
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc012/tasks/abc012_3

N = int(input())

num = 2025 - N

answer = [i for i in range(1, num+1) if num % i == 0]

for i in range(len(answer)):
    a = answer[i]
    b = num // answer[i]
    if a < 10 and b < 10:
        print(a,"x",b)

# AC
# Complete at 2023-07-15T21:25:39.880Z