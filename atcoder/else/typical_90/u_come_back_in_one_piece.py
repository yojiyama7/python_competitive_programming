from collections import deque

INF = float("inf")

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
	a, b = a-1, b-1
	g[a].add(b)
	# print(g)

ans = 0
dist = [INF]*N
for i in range(N):
	if dist[i] < INF:
		continue
	dist[i] = 0
	q = deque([i])
	while q:
		t = q.popleft()
		# print(t, g[t])
		t_dist = dist[t]

		for to in g[t]:
			if dist[to] == INF:
				dist[to] = t_dist + 1
				print(ans, dist)
				q.append(to)
			else:
				size = dist[to] - t_dist + 1
				ans += size*(size-1)//2

# ans = 0
# dist = [INF]*N
# dist[0] = 0
# q = deque([0])
# while q:
# 	t = q.popleft()
# 	t_dist = dist[t]

# 	for to in g[t]:
# 		if dist[to] == INF:
# 			dist[to] = t_dist + 1
# 			q.append(to)
# 		else:
# 			size = dist[to] - t_dist + 1
# 			print(size)
# 			ans += size*(size-1)//2

# print(ans)