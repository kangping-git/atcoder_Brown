# B. 投票
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc008/tasks/abc008_2

dic = {}
N = int(input())
for i in range(N):
    inp = input()
    if inp in dic:
        dic[inp] += 1
    else:
        dic[inp] = 1

m = -1
name = ""
for i in dic:
    if m < dic[i]:
        name = i
        m = dic[i]
print(name)

# AC
# Complete at 2023-07-15T11:20:08.489Z