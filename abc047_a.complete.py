# A. Fighting over Candies
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc047/tasks/abc047_a

ABC = list(map(int,input().split()))

for x in range(3):
    c = 0
    for y in range(3):
        if x == y:
            continue
        c += ABC[y]
    if ABC[x] == c:
        print("Yes")
        exit()
print("No")

# AC
# Complete at 2023-07-16T05:24:43.047Z