# A. プロコン
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc017/tasks/abc017_1

s1,e1 = map(int,input().split())
s2,e2 = map(int,input().split())
s3,e3 = map(int,input().split())
 
S1 = s1*(e1/10)
S2 = s2*(e2/10)
S3 = s3*(e3/10)
 
print(int(S1+S2+S3))

# AC
# Complete at 2023-07-15T21:39:48.899Z