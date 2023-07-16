# B. AtCoderトランプ
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc003/tasks/abc003_2

S = input()
T = input()
atcoder = list("atcoder")
flg = True
for i in range(len(S)):
    if S[i] == "@":
        if T[i] == "@":
            continue
        if not (T[i] in atcoder):
            flg = False
            break
        continue
    elif T[i] == "@":
        if not (S[i] in atcoder):
            flg = False
            break
        continue
    if S[i] != T[i]:
        flg = False
        break
if flg:
    print("You can win")
else:
    print("You will lose")

# AC
# Complete at 2023-07-08T10:32:09.799Z