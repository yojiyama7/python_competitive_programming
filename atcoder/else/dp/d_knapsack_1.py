# 20210123 100%

N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

WV = [(None, None)] + WV

# dp[i][j]: i番目までのもので 重さj**以下**の時の 価値の最大値
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
	w, v = WV[i]
	for j in range(W+1):
		if j - w >= 0:
			dp[i][j] = max(
				dp[i-1][j],
				dp[i-1][j-w] + v
			)
		else:
			dp[i][j] = dp[i-1][j]

# print(*dp, sep='\n')

print(dp[N][W])

