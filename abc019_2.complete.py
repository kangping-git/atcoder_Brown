# B. 高橋くんと文字列圧縮
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc019/tasks/abc019_2

s = input()
out = ""
count = 0
while count < len(s):
    char = s[count]
    _c = 0
    while count < len(s) and char == s[count]:
        count += 1
        _c += 1
    out += char + str(_c)
print(out)

# AC
# Complete at 2023-07-15T21:55:56.091Z