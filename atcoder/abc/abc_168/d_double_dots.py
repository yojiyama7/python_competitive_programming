from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    g[b].add(a)
    g[a].add(b)

mark = [-1]*N
mark[0] = 0
q = deque([0])
while q:
    t = q.popleft()

    for c in g[t]:
        if mark[c] == -1:
            mark[c] = t
            q.append(c)

print("Yes")
for m in mark[1:]:
    print(m+1)