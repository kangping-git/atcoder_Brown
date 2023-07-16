# A. テスト評価
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc028/tasks/abc028_a

N = int(input())
 
if N < 60:
    print("Bad")
elif N < 90:
    print("Good")
elif N < 100:
    print("Great")
else:
    print("Perfect")

# AC
# Complete at 2023-07-15T22:52:02.540Z