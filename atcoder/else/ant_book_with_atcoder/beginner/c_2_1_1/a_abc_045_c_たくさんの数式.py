# ABC 045 C - たくさんの数式
# https://atcoder.jp/contests/arc061/tasks/arc061_a

S = input()
len_S = len(S)

s = 0
for i in range(1<<(len_S-1)):
    t = S[0]
    for j in range(len_S-1):
        if (i>>j)%2:
            t += "+"
        t += S[j+1]
    s += eval(t)

print(s)