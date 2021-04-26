# ty evima

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
	a, b = a-1, b-1
	g[a].add(b)
	g[b].add(a)

visited = [0]*N
def visit(x, nodes):
	visited[x] = 1
	nodes.append(x)
	for to in g[x]:
		if visited[to]:
			continue
		visit(to, nodes)

def paint(x, nodes, colors):
	for to in g[nodes[x]]:
		if colors[to] == colors[nodes[x]]:
			return 0
	if x == len(nodes)-1:
		return (1)
	res = 0
	for i in range(3):
		colors[nodes[x+1]] = i
		res += paint(x+1, nodes, colors)
	colors[nodes[x+1]] = -1
	return (res)

ans = 1
for i in range(N):
	if visited[i]:
		continue
	nodes = []
	visit(i, nodes)
	colors = [-1]*N
	colors[i] = 0
	ans *= paint(0, nodes, colors) * 3

print(ans)