from collections import deque

INF = 10**20
MOD = 10**9+7

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

dist = [INF]*N
dist[0] = 0
q = deque([0])
while q:
    t = q.popleft()

    for c in g[t]:
        if dist[c] <= dist[t] + 1:
            continue
        dist[c] = dist[t]+1
        q.append(c)

# print(dist)

pattern = [0]*N
pattern[N-1] = 1
q = deque([N-1])
while q:
    t = q.popleft()

    for c in g[t]:
        if dist[c] != dist[t] - 1:
            continue
        if pattern[c] == 0:
            q.append(c)
        pattern[c] += pattern[t]
        pattern[c] %= MOD

print(pattern[0])
