# 20210123 20%
# 期待値, 確率問題よくわからん

N = int(input())
P = list(map(float, input().split()))

P = [None] + P

# dp[i][j]: i番目まで投げてj枚表が出る確率
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
	for j in range(i+1):
		if j >= 1:
			dp[i][j] = dp[i-1][j-1]*P[i] + dp[i-1][j]*(1-P[i])
		else:
			dp[i][j] = dp[i-1][j]*(1-P[i])

ans = 0
for j in range(N//2+1, N+1):
	ans += dp[N][j]
print(ans)
