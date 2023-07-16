# A. 長方形
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc027/tasks/abc027_a

les = list(map(int,input().split()))
X = -1
Y = -1
 
for i in range(len(les)):
    if X == -1:
        X = les[i]
    elif X != les[i]:
        Y = les[i]
 
if les.count(X) == 2:
    print(Y)
else:
    print(X)

# AC
# Complete at 2023-07-15T22:51:48.308Z