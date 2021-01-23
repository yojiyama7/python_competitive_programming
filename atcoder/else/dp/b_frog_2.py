# 20210123 100%

INF = float('inf')

N, K = map(int, input().split())
H = list(map(int, input().split()))

H = [None] + H

dp = [INF for _ in range(N+1)]
dp[1] = 0
for i in range(2, N+1):
	for j in range(1, K+1):
		if i-j >= 1:
			dp[i] = min(
				dp[i],
				dp[i-j] + abs(H[i] - H[i-j])
			)

print(dp[N])