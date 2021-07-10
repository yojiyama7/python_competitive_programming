N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    g[a].add(b)

cnt = 0
for i in range(N):
    visited = [0]*N
    q = [i]
    while q:
        t = q.pop()
        if visited[t]:
            continue
        visited[t] = 1
        for to in g[t]:
            q.append(to)
    cnt += sum(visited)

print(cnt)
