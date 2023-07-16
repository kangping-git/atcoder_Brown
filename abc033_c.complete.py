# C. 数式の書き換え
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc033/tasks/abc033_c

S = input()
lastAdd = True
MulList = [set([S[0]])]
i = 1
while i < len(S):
    if S[i] == "*":
        MulList[-1].add(S[i+1])
    else:
        MulList.append(set(S[i+1]))
    i += 2

count = 0
for i in range(len(MulList)):
    if not "0" in MulList[i]:
        count += 1
print(count)

# AC
# Complete at 2023-07-15T23:38:26.020Z