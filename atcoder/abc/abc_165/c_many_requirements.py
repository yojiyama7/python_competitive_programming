# 全探索GAMING
from itertools import combinations as combi

N, M, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(Q)]

#/##//####
# M-1+N C N
max_num = 0
for l in combi(range(M-1+N), N):
    x = [t-s for t, s in zip(l, range(N))]
    # print(x)
    score = sum(d for a, b, c, d in ABCD if x[b-1]-x[a-1] == c)
    max_num = max(max_num, score)

print(max_num)
