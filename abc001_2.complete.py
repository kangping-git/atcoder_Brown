# B. 視程の通報
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc001/tasks/abc001_2

def calculate_vv(visibility):
    if visibility < 100:
        vv = '00'
    elif visibility <= 5000:
        vv = zero(str(int(visibility / 100)))
    elif visibility <= 30000:
        vv = str(int(visibility / 1000) + 50)
    elif visibility <= 70000:
        vv = str(int((visibility / 1000 - 30) / 5 + 80))
    else:
        vv = '89'
    return vv

def zero(string):
    return "0" * (2 - len(string)) + string

m = int(input())
print(calculate_vv(m))

# AC
# Complete at 2023-07-08T10:15:58.783Z