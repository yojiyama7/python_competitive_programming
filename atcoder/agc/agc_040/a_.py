from itertools import groupby

S = input()

l = [0]*(S[0]=="<") + [len(list(g)) for k, g in groupby(S)] + [0]*(S[-1]==">")

s = 0
m = [0]*(len(l)//2)
for i in range(0, len(l)//2):
    a, b = l[i*2], l[i*2+1]
    m[i] = b
    if i >= 1:
        m[i-1] = min(m[i-1], a)
    s += int((a+1)*(a/2) + (b+1)*(b/2))

print(s-sum(m[:-1]))