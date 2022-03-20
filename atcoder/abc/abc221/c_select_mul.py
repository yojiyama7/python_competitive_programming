from itertools import permutations as permu

N = input()

l = list(N)
l.sort(reverse=True)

l_len = len(N)

ans = 0
for i in range(1<<l_len):
    s = ""
    t = ""
    for j, n in enumerate(l):
        if (i>>j)&1:
            s += n
        else:
            t += n
    if not s or not t:
        continue
    if s[0] == '0' or t[0] == '0':
        continue
    a, b = int(s), int(t)
    score = a*b
    ans = max(ans, score)

print(ans)
