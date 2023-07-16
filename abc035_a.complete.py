# A. テレビ
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc035/tasks/abc035_a

W,H = map(int,input().split())

if W//4 == H//3:
    print("4:3")
else:
    print("16:9")

# AC
# Complete at 2023-07-15T23:42:07.320Z