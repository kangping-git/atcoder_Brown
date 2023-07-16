# B. Unhappy Hacking (ABC Edit)
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc043/tasks/abc043_b

s = input()
S = ""
for i in s:
    if i == "0":
        S += "0"
    elif i == "1":
        S += "1"
    else:
        S = S[:-1]
print(S)

# AC
# Complete at 2023-07-16T04:36:43.503Z