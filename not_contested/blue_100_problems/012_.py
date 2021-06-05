# https://atcoder.jp/contests/abc002/tasks/abc002_4

from itertools import combinations as combi
N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for x, y in XY:
	x, y = x-1, y-1
	g[x].add(y)
	g[y].add(x)
# print(g)

ans = 0
for i in range(1<<N):
	l = [j for j in range(N) if (i>>j)&1]
	if all(y in g[x] for x, y in combi(l, 2)):
		# print(list(combi(l, 2)))
		ans = max(ans, len(l))
print(ans)
