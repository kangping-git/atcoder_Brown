# B. 錠
# Difficulty: grey
# URL: https://atcoder.jp/contests/abc013/tasks/abc013_2

def red(num):
    return (num + 1) % 10
def blue(num):
    return (num - 1) % 10

a = int(input())
b = int(input())

count = 0
_red = a
while _red != b:
    _red = red(_red)
    count += 1

_count = 0
_blue = a
while _blue != b:
    _blue = blue(_blue)
    _count += 1
print(min(count, _count))

# AC
# Complete at 2023-07-15T21:29:17.652Z