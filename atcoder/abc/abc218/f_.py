from collections import deque

INF = 10**18

N, M = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(M)]

edges = [(s-1, t-1) for s, t in ST]

g = [set() for _ in range(N)]
g_rev = [set() for _ in range(N)]
for s, t in edges:
    g[s].add(t)
    g_rev[t].add(s)

def bfs(g):
    dist = [INF]*N
    dist[0] = 0
    q = deque([0])
    while q:
        t = q.popleft()
        for to in g[t]:
            if dist[to] <= dist[t] + 1:
                continue
            dist[to] = dist[t] + 1
            q.append(to)
    return dist

def first(g):
    dist = bfs(g)
    nodes = [N-1]
    while nodes[-1] != 0:
        x = nodes[-1]
        flag = True
        for nei in g_rev[x]:
            # print((x, nei))
            if dist[nei] == dist[x] - 1:
                nodes.append(nei)
                flag = False
                break
        if flag:
            break
    # print(nodes)
    edges = set((nodes[i+1], nodes[i]) for i in range(len(nodes)-1))
    return (dist[N-1], edges)

def solve(g):
    return bfs(g)[N-1]

default, main_edges = first(g)
# print(default, main_edges)
for e in edges:
    if e in main_edges:
        s, t = e
        g[s].remove(t)
        ans = solve(g)
        g[s].add(t)
    else:
        ans = default
    print(-1 if ans == INF else ans)

################################

# # 最短経路に含まれる頂点はN個以下なので
# # 辺もN本未満だねぇ～～～～
# # こういう基礎基礎の知識は書きだして覚えてもいいな

# from collections import deque

# INF = 10**18

# N, M = map(int, input().split())
# ST = [list(map(int, input().split())) for _ in range(M)]

# g = [set() for _ in range(N)]
# g_rev = [set() for _ in range(N)]
# for s, t in ST:
#     s -= 1
#     t -= 1
#     g[s].add(t)
#     g_rev[t].add(s)

# dist = [INF]*N
# dist[0] = 0
# q = deque([0])
# while q:
#     t = q.popleft()
#     for to in g[t]:
#         if dist[to] <= dist[t] + 1:
#             continue
#         dist[to] = dist[t] + 1
#         q.append(to)

# dist_rev = [INF]*N
# dist_rev[N-1] = 0
# q = deque([N-1])
# while q:
#     t = q.popleft()
#     for to in g_rev[t]:
#         if dist_rev[to] <= dist_rev[t] + 1:
#             continue
#         dist_rev[to] = dist_rev[t] + 1
#         q.append(to)

# for s, t in ST:
#     s -= 1
#     t -= 1
#     ans = INF
#     for nei in g_rev[t]:
#         if nei == s:
#             continue
#         ans = min(ans, dist[nei] + 1)
#     ans += dist_rev[t]

# ################################

# # from collections import deque

# # INF = 10**18

# # N, M = map(int, input().split())
# # ST = [list(map(int, input().split())) for _ in range(M)]

# # g = [set() for _ in range(N)]
# # g_rev = [set() for _ in range(N)]
# # for s, t in ST:
# #     s -= 1
# #     t -= 1
# #     g[s].add(t)
# #     g_rev[t].add(s)

# # dist = [INF]*N
# # dist[0] = 0
# # q = deque([0])
# # while q:
# #     t = q.popleft()
    
# #     for to in g[t]:
# #         if dist[to] <= dist[t] + 1:
# #             continue
# #         dist[to] = dist[t] + 1
# #         q.append(to)

# # min_dist = dist[N-1]

# # print(dist)

# # ans = dict()
# # d = [sorted((dist[nei]+1, nei) for nei in g_rev[i]) for i in range(N)]
# # print(d)
# # for i, di in enumerate(d):
# #     if not di:
# #         continue
# #     dist_nei, nei = di[0]
# #     if len(di) == 1:
# #         k, v = ((nei, i), INF)
# #     else:
# #         k, v = ((nei, i), min_dist+(di[1][0]-dist_nei))
# #     ans[k] = v
# #     for dist_nei, nei in di[1:]:
# #         k, v = ((nei, i), min_dist)

# # for s, t in ST:
# #     s -= 1
# #     t -= 1
# #     if (s, t) in ans:
# #         x = ans[(s, t)]
# #         # if x == INF:
# #         #     x = -1
# #         print(x)
# #     else:
# #         print(-1)
