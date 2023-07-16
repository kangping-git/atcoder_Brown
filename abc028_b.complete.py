# B. 文字数カウント
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc028/tasks/abc028_b

S = input()
ABCDEF = list("ABCDEF")
count = []
for i in range(6):
    count.append(S.count(ABCDEF[i]))
print(*count)

# AC
# Complete at 2023-07-15T22:53:45.774Z