# B. 高橋君とパスワード
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc032/tasks/abc032_b

s = input()
k = int(input())
l = set()
for i in range(0,len(s)-k+1):
    l.add(s[i:i+k])
print(len(l))

# AC
# Complete at 2023-07-15T23:17:46.899Z