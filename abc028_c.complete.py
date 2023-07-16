# C. 数を3つ選ぶマン
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc028/tasks/abc028_c

ABCDE = list(map(int,input().split()))

t = set()
for x in range(5):
    for y in range(5):
        if x != y:
            for z in range(5):
                if y != z and x != z:
                    t.add(ABCDE[x] + ABCDE[y] + ABCDE[z])
t = list(t)
t.sort(reverse=True)
print(t[2])

# AC
# Complete at 2023-07-15T22:57:56.779Z