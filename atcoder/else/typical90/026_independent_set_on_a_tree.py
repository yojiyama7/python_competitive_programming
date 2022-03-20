from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

dist = [2]*N
dist[0] = 0
q = deque([0])
while q:
    t = q.popleft()

    for to in g[t]:
        if dist[to] != 2:
            continue
        dist[to] = (dist[t]+1)%2
        q.append(to)
    # print(dist)

even_odd = [[], []]
for i, d in enumerate(dist):
    even_odd[d].append(i)

l = max(even_odd, key=len)
ans = [li+1 for li in l][:N//2]

print(*ans)
