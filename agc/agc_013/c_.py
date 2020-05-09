# ちょい辛い、実装ゲーム
# 円形の二分探索ぇ、、

from bisect import bisect

N, L, T = map(int, input().split())
XW = [list(map(int, input().split())) for _ in range(N)]

XW = [(x, w-1) for x, w in XW]

d_rl = [[], []]
e_rl = [[], []]
for i, (x, w) in enumerate(XW):
    dr_dl[w].append(x)
    e_rl[w].append(i)
# dr, dl = d_rl
n_rl = [len(dr), len(dl)]

memo = [-1]*N
for i, (x, w) in enumerate(XW):
    other_e = e_rl[1-w]
    other_d = d_rl[1-w]
    other_n = n_rl[1-w]
    c = (x+2*T)//L * other_n
    c += bisect(other_d, (x+2*T)%L)
    c -= bisect(other_d, x)
    # memo[] = 
