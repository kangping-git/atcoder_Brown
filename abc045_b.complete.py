# B. Card Game for Three (ABC Edit)
# Difficulty: brown
# URL: https://atcoder.jp/contests/abc045/tasks/abc045_b

ABC = {"A": input().upper(), "B": input().upper(), "C": input().upper()}
H = "A"
while True:
    if len(ABC[H]) == 0:
        print(H)
        break
    t = H
    H = ABC[H][0]
    ABC[t] = ABC[t][1:]

# AC
# Complete at 2023-07-16T05:16:40.267Z