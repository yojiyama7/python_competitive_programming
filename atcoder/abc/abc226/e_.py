MOD = 998244353

N, M = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)

removed = [0 for _ in range(N)]
cnt = 0
for i in range(N):
    if removed[i]:
        continue
    visited = {i}
    edge = 0
    q = [i]
    while q:
        t = q.pop()
        for to in g[t]:
            if removed[to]:
                continue
            edge += 1
            if to in visited:
                continue
            visited.add(to)
            q.append(to)
    # print(visited, edge)
    if len(visited) != edge//2:
        print(0)
        exit()
    for v in visited:
        removed[v] = 1
    cnt += 1

ans = pow(2, cnt, MOD)
print(ans)
