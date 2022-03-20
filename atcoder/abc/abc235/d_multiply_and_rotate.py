# 到達不可能な場所に原理的にいけないようにする
# 1から考える
# and 小さいものからではなくBFSでやるべき(最短であることが確定するタイミングのため)

from collections import deque

INF = 10**18
A, N = map(int, input().split())

g = [set() for _ in range(10**6)]
for i in range(1, 10**6):
    if i*A < 10**6:
        g[i].add(i*A)
    if i >= 10 and i%10 != 0:
        s = str(i)
        x = int(s[-1] + s[:-1])
        g[i].add(x)

dist = [INF]*(10**6)
dist[1] = 0
q = deque([1])
while q:
    t = q.popleft()
    # print(t)
    for to in g[t]:
        if dist[to] <= dist[t] + 1:
            continue
        dist[to] = dist[t] + 1
        q.append(to)

# print(dist[:20])
ans = -1 if dist[N] == INF else dist[N]
print(ans)

################################

# # aftercontest WA
# # DFS だからよくない？　よくないね

# import sys
# sys.setrecursionlimit(10**8)

# INF = 10**18

# A, N = map(int, input().split())

# memo = [None]*(10**6)
# l = [0]*(10**6)
# def solve(i):
#     if i == 1:
#         return 0
#     if l[i]:
#         return INF
#     l[i] = 1
#     if memo[i] == None:
#         ans = INF
#         if i%A == 0:
#             score = solve(i//A) + 1
#             ans = min(ans, score)
#         s = str(i)
#         if len(s) >= 2 and s[1] != '0':
#             score = solve(int(s[1:]+s[0])) + 1
#             ans = min(ans, score)
#         memo[i] = ans
#     l[i] = 0
#     return memo[i]

# x = solve(N)
# ans = -1 if x == INF else x
# print(ans)
