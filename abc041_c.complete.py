# C. 背の順
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc041/tasks/abc041_c

N = int(input())
a = list(map(lambda x:{"index":x[0],"tall":int(x[1])},enumerate(input().split())))
a.sort(key=lambda x:x["tall"],reverse=True)
for i in range(N):
    print(a[i]["index"] + 1)

# AC
# Complete at 2023-07-16T04:26:41.628Z