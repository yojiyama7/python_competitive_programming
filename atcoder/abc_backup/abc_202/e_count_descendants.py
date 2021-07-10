# 深さを軸に、子孫を判定

# [公式 KoD](https://atcoder.jp/contests/abc202/editorial/1864)
# わかった とりあえずこれで実装してみる (本番にここまで証明する必要はないだろうが理解はしておきたい)
# [hamayanhamayan](https://blog.hamayanhamayan.com/entry/2021/05/22/225525)
# 後半(帰着問題をいかに解くか) わからん
# [kanpurin](https://kanpurin.hatenablog.com/entry/2021/05/22/231444)
# お気持ちだけしかわからん
# [TumoiYorozu](https://atcoder.jp/contests/abc202/editorial/1906)
# ウェーブレット木ねぇ、、、ふぅん、、、

from bisect import bisect_left
import sys
sys.setrecursionlimit(10**8)

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
UD = [list(map(int, input().split())) for _ in range(Q)]

g = [set() for _ in range(N)]
for i, p in enumerate(P, start=1):
	p = p-1
	g[p].add(i)

depth = [None]*N
depth[0] = 0
pre = [None]*N
post = [None]*N
layer = [[] for _ in range(N)]

visit_num = 0
def dfs(i):
	global visit_num
	pre[i] = visit_num
	visit_num += 1
	# print(i, depth[i])
	layer[depth[i]].append(pre[i])
	for to in g[i]:
		depth[to] = depth[i] + 1
		dfs(to)
	post[i] = visit_num
	visit_num += 1

dfs(0)
# print(depth, pre, post, layer)

for u, d in UD:
	u, d = u-1, d
	l, r = pre[u], post[u]
	# print(u, (l, r), d, layer[d])
	m = layer[d]
	ans = bisect_left(m, r) - bisect_left(m, l)
	print(ans)

################################

# # u から根への最短パス上(端点も含む)に頂点 Ui が存在する。
# # >>> Uiの子孫(自身でも良い)である
# # u から根への最短パスに含まれる辺の数がちょうど Di である。
# # >>> Di: 深さ
# # u の個数

# # d[u] > d[i]: 0
# # d[u] == d[i]: 1
# # d[u] < d[i]: 1

# # Diのでかいクエリから答える？

# # 高速化の部分が全くわからん

# # これは冷え

# from collections import deque
# import sys
# sys.setrecursionlimit(10**8)

# # from itertools import chain
# # INF = float("inf")

# N = int(input())
# P = list(map(int, input().split()))
# Q = int(input())
# UD = [list(map(int, input().split())) for _ in range(Q)]
# # N = 2*10**5
# # P = list(range(1, N))
# # UD = list(chain(*[[(i, j) for j in range(200)] for i in range(1000)]))
# # Q = len(UD)

# g = [set() for _ in range(N)]
# for i, p in enumerate(P, start=1):
# 	p = p-1
# 	g[p].add(i)

# depth = [None]*N
# depth[0] = 0
# q = deque([0])
# while q:
# 	t = q.popleft()
# 	t_depth = depth[t]
# 	for to in g[t]:
# 		depth[to] = t_depth + 1
# 		q.append(to)

# memo = [dict() for _ in range(N)]
# def solve(x, remain):
# 	if remain == 0:
# 		return 1
# 	if remain in memo[x]:
# 		return memo[x][remain]
# 	ans = 0
# 	for to in g[x]:
# 		ans += solve(to, remain-1)
# 	memo[x][remain] = ans
# 	return memo[x][remain]

# for u, d in UD:
# 	u, d = u-1, d
# 	if depth[u] > d:
# 		print(0)
# 		continue
# 	if depth[u] == d:
# 		print(1)
# 		continue
# 	# depth[u] < d
# 	ans = solve(u, d-depth[u])
# 	print(ans)
