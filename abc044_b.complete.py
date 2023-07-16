# B. Beautiful Strings
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc044/tasks/abc044_b

w = input()
W = set(list(w))
for i in w:
    if w.count(i) % 2 == 1:
        print("No")
        exit()
print("Yes")

# AC
# Complete at 2023-07-16T04:41:14.713Z