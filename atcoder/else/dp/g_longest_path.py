# 20210123 40%

# もらう, 配る(for文をつかってdpの値を求める)だとむずい
# グラフ系はメモ化再帰?
# トポロジカルソート とは, またそれを利用してfor文dpする方法とは
import sys

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N+1)]
for x, y in XY:
	g[x].add(y)

# x を 始点とする 最長経路
dp = [-1 for _ in range(N+1)]
def solve(x):
	if len(g[x]) == 0:
		return (0)
	if dp[x] == -1:
		dp[x] = max(solve(child) + 1 for child in g[x])
	return (dp[x])

ans = max(solve(x) for x in range(1, N+1))
# print(dp)
print(ans)
