# ワーシャルフロイド -> は？？？？？？？？
# グラフを制限している状態から徐々に本来のグラフにしていく感覚?
# O(V**3)

from heapq import *
from itertools import chain

INF = float('inf')

# def dijkstra(s, n, g):
#     dist = [INF]*n
#     dist[s] = 0
#     is_done = [False]*n
#     q = [(0, s)]
#     while q:
#         print(q)
#         _, v = heappop(q)
#         is_done[v] = True
#         for to, cost in enumerate(g[v]):
#             if is_done[to] == False and dist[v] + cost < dist[to]:
#                 dist[to] = dist[v] + cost
#                 heappush(q, (dist[to], to))
#     return dist

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

# print(*C, sep="\n")
# print(*list(zip(*C)), sep="\n")

d = [[C_ij for C_ij in C_i] for C_i in C]
# この順序 (経由する頂点, 始点, 終点) であることの意味
for k in range(10):
    for i in range(10):
        for j in range(10):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

ans = sum([d[a][1] for a in chain(*A) if a != -1])
print(ans)

################################

# ワーシャルフロイド法などで最短経路探索もあり。
# dijkstraもありか、scipy(サイパイ)すごそう。
# 最短経路むずい。

################################

# from itertools import permutations as per

# H, W = map(int, input().split())
# C = [list(map(int, input().split())) for _ in range(10)]
# A = [list(map(int, input().split())) for _ in range(H)]

# これが俗にいうbitDPでは、、？
# dp[i(1<<10)][j(10)][k(10)] = jからi(bit flags)を通ってkにできる最小コスト
# 疲れた。

# dp = [[[10**18 for _ in range(10)] for _ in range(10)] for _ in range(1<<10)]
# dp 
# for j in range(10):
#     for k in range(10):
