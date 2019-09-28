# JOI 2007 本選 C ダーツ
# https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
# AOJ 0529
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0529

from bisect import bisect_right

N, M = map(int, input().split())
P = [0] + [int(input()) for _ in range(N)]

pairs = []
for i, p_i in enumerate(P):
    for p_j in P[i:]:
        pairs.append(p_i+p_j)
pairs = sorted(set(pairs))

max_p = 0
for pair in pairs:
    if pair > M:
        continue
    x = bisect_right(pairs, M-pair)-1
    # print(pair, pairs[x], M-pair)
    max_p = max(max_p, pair+pairs[x])

print(max_p)