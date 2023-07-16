# B. 町の合併
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc033/tasks/abc033_b

N = int(input())

s = 0
dic = {}

for i in range(N):
    S,P = input().split()
    s += int(P)
    dic[S] = int(P)

for i in dic.keys():
    if dic[i] * 2 > s:
        print(i)
        exit()
print("atcoder")

# AC
# Complete at 2023-07-15T23:21:45.840Z