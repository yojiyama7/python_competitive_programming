from itertools import chain, starmap
from itertools import accumulate as acc

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

s = set()
for a, b in AB:
    s.add(a)
    s.add(a+b)
l = sorted(s)

d = dict((li, i) for i, li in enumerate(l))

p = [0]*len(l)
for a, b in AB:
    p[d[a]] += 1
    p[d[a+b]] -= 1

p_acc = list(acc(p))[:-1]

# print(l)
# print(p_acc)
ans = [0]*(N+1)
for i, pi in enumerate(p_acc):
    ans[pi] += l[i+1] - l[i]

print(*ans[1:])
