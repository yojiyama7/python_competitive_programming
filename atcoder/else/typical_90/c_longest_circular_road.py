from collections import deque

INF = float('inf')

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

g = [set() for _ in range(N)]
for a, b in AB:
	a, b = a-1, b-1
	g[a].add(b)
	g[b].add(a)

def bfs_farthest(s):
	dist = [INF]*N
	dist[s] = 0
	q = deque([s])
	while q:
		t = q.popleft()
		t_dist = dist[t]

		for to in g[t]:
			if dist[to] <= t_dist + 1:
				continue
			dist[to] = t_dist + 1
			q.append(to)
	idx = max(range(N), key=lambda x: dist[x])
	return (idx, dist[idx])

s, _ = bfs_farthest(0)
_, max_dist = bfs_farthest(s)

ans = max_dist + 1
print(ans)
