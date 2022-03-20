from heapq import *

INF = 10**18

class HeapMin:
    def __init__(self, l=[], key=lambda x:x):
        self.key = key
        self.l = [(self.key(l_i), l_i) for l_i in l]
        heapify(self.l)

    def push(self, v):
        heappush(self.l, (self.key(v), v))

    def pop(self):
        _, r = heappop(self.l)
        return r

    def __bool__(self):
        return len(self.l) > 0

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

g = [dict() for _ in range(N)]
for a, b, c in ABC:
    a -= 1
    b -= 1
    if b not in g[a]:
        g[a][b] = INF
    g[a][b] = min(g[a][b], c)

def dijkstra(start):
    dist = [INF for _ in range(N)]
    dist[start] = 0
    q = HeapMin([(start, 0)])
    while q:
        t, t_dist = q.pop()
        if dist[t] != t_dist:
            continue
        for to, cost in g[t].items():
            if dist[to] <= t_dist + cost:
                continue
            dist[to] = t_dist + cost
            q.push((to, dist[to]))
    return dist

d = [dijkstra(i) for i in range(N)]
for i in range(N):
    ans = INF
    for j in range(N):
        if i == j:
            if i in g[i]:
                score = g[i][i]
                ans = min(ans, score)
        else:
            score = d[i][j] + d[j][i]
            ans = min(ans, score)
    if ans == INF:
        print(-1)
    else:
        print(ans)
