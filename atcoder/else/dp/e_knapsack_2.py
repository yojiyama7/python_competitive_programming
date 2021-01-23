# 20210123 60%

INF = float('inf')

N, W = map(int, input().split())
WV = [(None, None)] + [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i番目までの商品で 価値j**以上**の時の最小の重さ
dp = [[INF for _ in range(1000*N+2)] for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
	w, v = WV[i]
	for j in range(1000*N+1):
		if j-v >= 0:
			dp[i][j] = min(
				dp[i-1][j],
				dp[i-1][j-v] + w,
			)
		else:
			dp[i][j] = dp[i-1][j]
ans = 1000*N+1
while dp[i][ans] > W:
	ans -= 1
print(ans)
