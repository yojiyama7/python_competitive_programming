# スマートに、テンプレ的に書く方法を知りたい

# 強連結成分(SCC) で分割する
# 強連結成分分割
# 1. 適当な頂点から深さ優先探索で帰りがけに番号を振る。
# (最初に選んだ適当な頂点が最大になる)
# これを全ての頂点に番号が振られるまで繰り返す。
# (全ての頂点に別の番号が振られるようにする)
# 2. グラフのアークを逆にしたグラフをGtとする
# Gtにおいて番号が最大の頂点から深さ優先探索をする
# **参考を読め**
# 参考: https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html

import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
gt = [set() for _ in range(N)]
for a, b in AB:
	a, b = a-1, b-1
	g[a].add(b)
	gt[b].add(a)

visited = [0]*N
g_upstream = [-1]*N
level = 0
def dfs(i):
	global level
	if visited[i]:
		return
	visited[i] = 1
	to_list = [to for to in g[i] if visited[to] == 0]
	if to_list:
		for to in to_list:
			dfs(to)
	else:
		pass
	g_upstream[i] = level
	level += 1

for i in range(N):
	if visited[i]:
		continue
	dfs(i)

# print(g_upstream)
gt_downstream = g_upstream

visited2 = [0]*N
def dfs2(i):
	if visited2[i]:
		return 0
	visited2[i] = 1
	ret = 1
	for to in gt[i]:
		ret += dfs2(to)
	return (ret)

ans = 0
for i in sorted(range(N), key=lambda x: gt_downstream[x], reverse=True):
	if visited2[i]:
		continue
	size = dfs2(i)
	# print(size)
	ans += size * (size-1) // 2

print(ans)

################################

# from collections import deque

# INF = float("inf")

# N, M = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]

# g = [set() for _ in range(N)]
# for a, b in AB:
# 	a, b = a-1, b-1
# 	g[a].add(b)
# 	# print(g)

# ans = 0
# dist = [INF]*N
# for i in range(N):
# 	if dist[i] < INF:
# 		continue
# 	dist[i] = 0
# 	q = deque([i])
# 	while q:
# 		t = q.popleft()
# 		# print(t, g[t])
# 		t_dist = dist[t]

# 		for to in g[t]:
# 			if dist[to] == INF:
# 				dist[to] = t_dist + 1
# 				print(ans, dist)
# 				q.append(to)
# 			else:
# 				size = dist[to] - t_dist + 1
# 				ans += size*(size-1)//2

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