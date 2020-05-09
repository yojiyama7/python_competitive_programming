import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

N, M, R = map(int, input().split())
E = list(map(int, input().split()))
ABC = [list(map(int, input().split())) for _ in range(M)]

d = np.zeros_like((N+1, N+1))
# np.full_like(d, 10**)
for a, b, c in ABC:
    d[a][b] = c
    d[b][a] = c

shortest_path(