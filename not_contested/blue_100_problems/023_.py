# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

from bisect import bisect_right

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]

P = [0]+P

pairs = set()
for i, p1 in enumerate(P):
    for p2 in P[i:]:
        pairs.add(p1+p2)
pairs = sorted(pairs)
# print(pairs)

max_num = 0
for x in pairs:
    if x > M:
        continue
    idx = bisect_right(pairs, M-x)
    y = pairs[idx-1]
    # print([x, y], x+y)
    max_num = max(max_num, x+y)

print(max_num)
