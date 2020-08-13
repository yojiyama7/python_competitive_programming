from itertools import accumulate

N = int(input())
D = [list(map(int, input().split(" "))) for _ in range(N)]
Q = int(input())
P = [int(input()) for _ in range(Q)]

l = [[0]*(N+1)] + [[0]+list(accumulate(d)) for d in D]
l = list(zip(*[list(accumulate(l_i)) for l_i in zip(*l)]))

def cum_sum(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return l[y2+1][x2+1] - l[y2+1][x1] - l[y1][x2+1] + l[y1][x1]

r = [0]*(N**2+1)
for x1 in range(N):
    for y1 in range(N):
        for x2 in range(x1, N):
            for y2 in range(y1, N):
                size = (x2-x1+1)*(y2-y1+1)
                point = cum_sum((x1, y1), (x2, y2))
                r[size] = max(r[size], point)
# print(r)
for i in range(1, N**2+1):
    r[i] = max(r[i-1], r[i])
# print(r)

for p in P:
    print(r[p])