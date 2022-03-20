from heapq import *

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
# N, M = 100000, 100000-1
# ABC = [(i, i+1, i) for i in range(1, M+1)]

INF = float('inf')

class HeapMin:
    def __init__(self, l):
        self.l = l
        heapify(self.l)

    def pop(self):
        return heappop(self.l)

    def push(self, v):
        heappush(self.l, v)

g = [set() for _ in range(N)]
for a, b, c in ABC:
	a, b, c = a-1, b-1, c
	g[a].add((b, c))
	g[b].add((a, c))

d1 = [INF]*N
d1[0] = 0
q = HeapMin([(0, 0)])
while q.l:
	t_dist, t = q.pop()
	if t_dist > d1[t]:
		continue

	for to, cost in g[t]:
		if d1[to] <= t_dist + cost:
			continue
		d1[to] = t_dist + cost
		q.push([d1[to], to])

d2 = [INF]*N
d2[N-1] = 0
q = HeapMin([(0, N-1)])
while q.l:
	t_dist, t = q.pop()
	if t_dist > d2[t]:
		continue

	for to, cost in g[t]:
		# print([to, cost])
		if d2[to] <= t_dist + cost:
			continue
		d2[to] = t_dist + cost
		q.push([d2[to], to])

for k in range(N):
	print(d1[k] + d2[k])
