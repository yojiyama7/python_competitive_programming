from collections import deque

M = int(input())
UV = [list(map(int, input().split())) for _ in range(M)]
P = tuple(map(int, input().split()))

g = [set() for _ in range(9)]
for u, v in UV:
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)

first = [8]*9
for i, p in enumerate(P):
    p -= 1
    first[p] = i
first_tpl = tuple(first)

dist = dict()
dist[first_tpl] = 0
q = deque([first])
while q:
    t = q.popleft()
    idx_empty = t.index(8)
    for to in g[idx_empty]:
        s = t[:]
        s[idx_empty], s[to] = s[to], s[idx_empty]
        if tuple(s) in dist:
            continue
        dist[tuple(s)] = dist[tuple(t)] + 1
        q.append(s)

goal = tuple(range(9))
if goal in dist:
    print(dist[goal])    
else:
    print(-1) 