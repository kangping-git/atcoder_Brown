# B. ディスプレイ
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc038/tasks/abc038_b

HW_1 = list(map(int,input().split()))
HW_2 = list(map(int,input().split()))
for x in range(2):
    for y in range(2):
        if HW_1[x] == HW_2[y]:
            print("YES")
            exit()
print("NO")
# AC
# Complete at 2023-07-16T03:32:24.202Z