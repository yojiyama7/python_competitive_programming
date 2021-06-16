# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja

from collections import deque

INF = float('inf')

N = int(input())
UKV = [list(map(int, input().split())) for _ in range(N)]

g = [set() for _ in range(N)]
for u, _, *v in UKV:
    u -= 1
    g[u] = {v_i-1 for v_i in v}

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

for i, d in enumerate(dist):
    print(i+1, (-1 if d == INF else d))
