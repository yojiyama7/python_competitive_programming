# 4 5 5
# 1 2 4
# 1 3 2
# 3 2 1
# 2 4 2
# 3 4 5
# 1
# 1 4

# >>> 0

################################

# うーん解けなかった。
# dijkstraができない
# dijkstraは距離が最小のものから順に処理していくことを知った。
# 確かにそうしないと 辺の数が多く距離の小さいもの が最小経路に慣れない時がある。
# 最小経路がL以下の部分に長さ1の辺のあるグラフを作り直すと、bfsできる。
# from collections import deque

from heapq import *

N, M, L = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
ST = [list(map(int, input().split())) for _ in range(Q)]

d = [[] for _ in range(N)]
for a, b, c in ABC:
    d[a-1].append((b-1, c))
    d[b-1].append((a-1, c))

# print(d)

# スタートをiにしてdijkstra * N
a_to_b = []
for i in range(N):
    # (ここまでの燃料補給回数, 使った燃料(L-残り燃料))
    i_to_b = [10**24 for _ in range(N)]
    i_to_b[i] = 10**24

    visited = [0]*N
    
    q = [i]
    while q:
        # print(q)
        ti = heappop(q)
        tc = i_to_b[ti]

        for ni in d[ti]:
            if visited[ni]:
                continue
            if tm+nm <= L:
                n_bm = (tb, tm+nm)
            elif nm <= L:
                n_bm = (tb+1, nm)
            else:
                n_bm = (10**24, 10**24)
            # print(i, (ni, ), (tb, tm), n_bm, i_to_b[ni])
            i_to_b[ni] = min(i_to_b[ni], n_bm)
            if visited[ni] == 0:
                heappush(q, (i_to_b[ni], ni))
                visited[ni] = 1
            # print(i_to_b)
        visited[ti] = 2
    a_to_b.append(i_to_b)
    # print(i_to_b)

# print(a_to_b)

for s, t in ST:
    r = a_to_b[s-1][t-1][0]
    print(-1 if r == 10**24 else r)