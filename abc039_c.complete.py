# C. ピアニスト高橋君
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc039/tasks/abc039_c

kenban = list("WBWBWWBWBWBW")
l = [
    "Do",
    "Do",
    "Re",
    "Re",
    "Mi",
    "Fa",
    "Fa",
    "So",
    "So",
    "La",
    "La",
    "Si",
]

S = input()
i = 0
while S[:len(kenban)] != "".join(kenban):
    kenban.append(kenban[0])
    del kenban[0]
    i += 1
print(l[i % len(kenban)])
# AC
# Complete at 2023-07-16T03:45:01.848Z