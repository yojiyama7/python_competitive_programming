<<<<<<< HEAD
# numpy, scipy での最短経路探索

# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import floyd_warshall
=======
import heapq

class HeapQueue:
    def __init__(self, l=[], key=lambda x: x):
        self.key = key
        self.l = heapq.heapify([(self.key(l_i), l_i) for l_i in l])
    
    def pop(self):
        _, v heapq.heappop(self.l):
        return v
    
    def push(self, v):
        heapq.heappush(self.l, (self.key(v), v))
    
    def __bool__(self):
        return bool(self.l)

N, M = map(int, input().split())
UVL = [list(map(int, input().split())) for _ in range(M)]

graph = [[10**18 for _ in range(300)] for _ in range(300)]
start_goal = set()
for u, v, l in UVL:
    u, v = u-1, v-1
    graph[u][v] = l
    graph[v][u] = l
    if u == 0:
        start_goal.add(v)

for start in start_goal:


################################

# 頂点1に属した頂点たちから、2つ選んで最短ルートさがして、その2頂点の頂点1まで距離を足す
# 全通りやって最短を出力 までは見たことあるんだけど
# 実装がねぇ、、、

# N, M = map(int, input().split(" "))
# UVL = [tuple(map(int, input().split(" "))) for _ in range(m)]
>>>>>>> 4108602f3a85210cd5f3a97b4c71ef3cde2a806d

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
