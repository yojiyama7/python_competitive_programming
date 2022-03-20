################################

# # ダイクストラ書けん

# from heapq import *

# Iints = list(map(int, input().split()))

# N, M, X, Y = Iints()
# ABTK = [Iints() for _ in range(M)]

# start, goal = X-1, Y-1

# g = [set() for _ in range(N)]
# for a, b, t, k in ABTK:
#     a, b, t, k = a-1, b-1, t, k
#     g[a].add((b, t, k))
#     g[b].add((a, t, k))

# dist = [INF]*N
# dist[start] = 0
# q = [0]
# while q:
