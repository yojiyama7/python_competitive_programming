# ABC 079 C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c

ABCD = input()

for i in range(1<<3):
    t = ABCD[0]
    for j in range(3):
        t += "+" if (i>>j)%2 else "-"
        t += ABCD[j+1]
    if eval(t) == 7:
        print(t+"=7")
        exit()