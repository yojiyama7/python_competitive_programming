# ワーシャルフロイド最強卍

INF = float("inf")

N, M = map(int, input().split())
UVL = [list(map(int, input().split())) for _ in range(M)]

dist = [[INF for j in range(N)] for i in range(N)]
h = set()
for u, v, l in UVL:
	u, v = u-1, v-1
	if u == 0:
		h.add((v, l))
	elif v == 0:
		h.add((u, l))
	else:
		dist[u][v] = l
		dist[v][u] = l

for k in range(N):
	for i in range(N):
		for j in range(N):
			if dist[i][j] > dist[i][k] + dist[k][j]:
				dist[i][j] = dist[i][k] + dist[k][j]

min_num = INF
for s, s_cost in h:
	for g, g_cost in h:
		if s == g:
			continue
		min_num = min(
			s_cost + dist[s][g] + g_cost,
			min_num
		)
print(-1 if min_num == INF else min_num)

################################

# もしかしてワーシャルフロイドのみ許される？

# from heapq import *

# class HeapMin:
#     def __init__(self, l=[], key=lambda x:x):
#         self.key = key
#         self.l = [(self.key(l_i), l_i) for l_i in l]
#         heapify(self.l)

#     def push(self, v):
#         heappush(self.l, (self.key(v), v))

#     def pop(self):
#         _, r = heappop(self.l)
#         return r

#     def __bool__(self):
#         return len(self.l) > 0

# INF = float("inf")

# N, M = map(int, input().split())
# UVL = [list(map(int, input().split())) for _ in range(M)]

# g = [set() for _ in range(N)]
# h = set()
# h_dist = [INF]*N
# for u, v, l in UVL:
# 	u, v = u-1, v-1
# 	if u == 0:
# 		h.add(v)
# 		h_dist[v] = l
# 	else:
# 		g[u].add((v, l))
# 	if v == 0:
# 		h.add(u)
# 		h_dist[u] = l
# 	else:
# 		g[v].add((u, l))

# min_num = INF
# for start in h:
# 	dist = [INF]*N
# 	dist[start] = 0
# 	q = HeapMin([(0, start)])
# 	while q:
# 		t_dist, t = q.pop()
# 		if t_dist > dist[t]:
# 			continue
# 		for to, cost in g[t]:
# 			if to == 0:
# 				continue
# 			if dist[to] < t_dist + cost:
# 				continue
# 			dist[to] = t_dist + cost
# 			q.push((dist[to], to))
# 	for goal in h:
# 		if start == goal:
# 			continue
# 		# print([start, goal, dist[goal]])
# 		min_num = min(
# 			h_dist[start] + dist[goal] + h_dist[goal],
# 			min_num
# 		)
# print(-1 if min_num == INF else min_num)

################################

# numpy, scipy での最短経路探索

# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import floyd_warshall

# N, M = map(int, input().split())
# UVL = [list(map(int, input().split())) for _ in range(M)]

# q = dict()
# g = [[10**18]*N for _ in range(N)]
# for u, v, l in UVL:
#     u, v = u-1, v-1
#     if u == 0:
#         q[v] = l
#     else:
#         g[u][v] = l
#         g[v][u] = l
# g = csr_matrix(g)
# print(g)
# d = floyd_warshall(g)

# print(d)

################################

# # python だと速度が足りない?

# from heapq import *
# from itertools import chain

# class HeapQueue:
#     def __init__(self, l=[], key=lambda x:x):
#         self.key = key
#         self.l = [(self.key(l_i), l_i) for l_i in l]
#         heapify(self.l)

#     def push(self, v):
#         heappush(self.l, (self.key(v), v))
    
#     def pop(self):
#         _, r = heappop(self.l)
#         return r
    
#     def __bool__(self):
#         return len(self.l) > 0

# # N, M = map(int, input().split())
# # UVL = [tuple(map(int, input().split())) for _ in range(M)]
# N = 300
# UVL = list(chain(*[[(i, j, 2) for j in range(i+1, N+1)] for i in range(1, N+1)]))

# d = [[10**18 for _ in range(N)] for _ in range(N)]
# g = [set() for _ in range(N)]
# for u, v, l in UVL:
#     u, v = u-1, v-1
#     d[u][v] = l
#     d[v][u] = l
#     g[u].add(v)
#     g[v].add(u)

# # print(p, g)

# # N(N(N+2))

# min_num = 10**18

# for start in g[0]:
#     # print(start, "s")
#     dist = [10**18]*N
#     dist[start] = 0
#     q = HeapQueue([start], key=lambda x: dist[x])
#     while q:
#         t = q.pop()
#         t_dist = dist[t]

#         for c in g[t]:
#             if c == 0:
#                 continue
#             if t_dist + d[t][c] < dist[c]:
#                 # print(dist)
#                 dist[c] = t_dist + d[t][c]
#                 q.push(c)
#                 # print(t, i)
#     # print(start, dist)
#     h_to_s = d[0][start]
#     for goal in g[0]:
#         if goal <= start:
#             continue
#         s_to_g = dist[goal] 
#         g_to_h = d[goal][0]
#         cost = h_to_s + s_to_g + g_to_h
#         # print(cost, (start, goal), (h_to_s, s_to_g, g_to_h))
#         min_num = min(cost, min_num)

# print(min_num if min_num < 10**18 else -1)

################################

# # 頂点1に属した頂点たちから、2つ選んで最短ルートさがして、その2頂点の頂点1まで距離を足す
# # 全通りやって最短を出力 までは見たことあるんだけど
# # 実装がねぇ、、、

# N, M = map(int, input().split(" "))
# UVL = [tuple(map(int, input().split(" "))) for _ in range(m)]
