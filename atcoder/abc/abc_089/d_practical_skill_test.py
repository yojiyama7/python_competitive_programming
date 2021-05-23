from itertools import accumulate
from bisect import bisect

H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

q = [[] for _ in range(D)]
for y, a in enumerate(A):
    for x, s in enumerate(a):
        q[s%D].append((s, x, y))

q = [sorted(q_i) for q_i in q]
# print(q)
t = [[q_j[0] for q_j in q_i] for q_i in q]
p = []
for q_i in q:
    p.append([])
    bx, by = 0, 0
    for q_j in q_i:
        _, x, y = q_j
        p[-1].append(abs(x-bx)+abs(y-by))
        bx, by = x, y
    p[-1] = [0] + list(accumulate(p[-1][1:]))

# print(p)
# print(t)

for l, r in LR:
    start = bisect(t[l%D], l)-1
    end = bisect(t[l%D], r)-1
    print(p[l%D][end]-p[l%D][start])
    # print(start, end, t[l%D], p[l%D])
