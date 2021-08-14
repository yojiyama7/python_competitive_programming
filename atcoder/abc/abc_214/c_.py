from heapq import *

INF = 10**18

class HeapMin:
    def __init__(self, l=[], key=lambda x:x):
        self.key = key
        self.l = [(self.key(l_i), l_i) for l_i in l]
        heapify(self.l)

    def push(self, v):
        heappush(self.l, (self.key(v), v))

    def pop(self):
        _, r = heappop(self.l)
        return r

    def __bool__(self):
        return len(self.l) > 0

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

g = [set() for _ in range(N+1)]
for i, s in enumerate(S):
    g[i].add(((i+1)%N, s))
for i, t in enumerate(T):
    g[N].add((i, t))

# print(g)

dist = [INF]*(N+1)
dist[N] = 0
q = HeapMin([(0, N)])
while q:
    dist_t, t = q.pop()
    if dist_t > dist[t]:
        continue
    for to, cost in g[t]:
        if dist[to] <= dist_t + cost:
            continue
        dist[to] = dist[t] + cost
        q.push((dist[t] + cost, to))
    # print(dist, q.l)

print(*dist[:N], sep='\n')
