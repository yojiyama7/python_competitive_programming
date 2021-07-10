INF = float('inf')

N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N-1)]
Q, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(Q)]

K -= 1

g = [set() for _ in range(N)]
for a, b, c in ABC:
    a, b, c = a-1, b-1, c
    g[a].add((b, c))
    g[b].add((a, c))

dist = [INF]*N
dist[K] = 0
q = [K]
while q:
    t = q.pop()
    for to, cost in g[t]:
        if dist[to] <= dist[t] + cost:
            continue
        dist[to] = dist[t] + cost
        q.append(to)

# print(dist)

for x, y in XY:
    x, y = x-1, y-1
    print(dist[x] + dist[y])
