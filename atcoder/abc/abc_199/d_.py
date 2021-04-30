from collections import deque

INF = float("inf")

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    g[a].add(b)
    g[b].add(a)

# 実装むずくて泣いちゃった
# def solve(l):
#     if len(l) == 1:
#         return 3
#     remain 
#     for i in remain

score = 1
is_visited = [0]*N
for i in range(N):
    if is_visited[i]:
        continue
    is_visited[i] = 1
    l = [i]
    q = deque([i])
    while q:
        # print(q)
        t, s = q.popleft()

        for to in g[t]:
            # print(t, to)
            if is_visited[to]:
                continue
            # print(to)
            is_visited[to] = 1
            q.append(to)
            l.append(to)
    score *= solve(l)

print(score)

################################

# from collections import deque

# INF = float("inf")

# N, M = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]

# g = [set() for _ in range(N)]
# for a, b in AB:
#     a, b = a-1, b-1
#     g[a].add(b)
#     g[b].add(a)

# dist = [INF]*N
# for i in range(N):
#     if dist[i] < INF:
#         continue
#     q = deque([i])
#     dist[i] = 0
#     while q:
#         # print(q)
#         t = q.popleft()
#         t_dist = dist[t]

#         for to in g[t]:
#             # print(t, to)
#             if dist[to] <= t_dist + 1:
#                 continue
#             # print(to)
#             dist[to] = t_dist + 1
#             q.append(to)

# l = sorted(range(N), key=lambda x: dist[x])
# # print(dist, l)
# # print(l)

# cnt = [-1]*N
# score = 1
# for l_i in l:
#     cnt[l_i] = max(0, 3 - sum(cnt[to] > -1 for to in g[l_i]))
#     score *= cnt[l_i]

# print(score)
