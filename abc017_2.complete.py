# B. choku語
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc017/tasks/abc017_2

choku = ["ch","o","k","u"]
count = 0
X = input()
while count < len(X):
    if X[count:count+2] == choku[0]:
        count += 2
    elif X[count] in choku[1:]:
        count += 1
    else:
        print("NO")
        exit()
print("YES")

# AC
# Complete at 2023-07-15T21:48:27.329Z