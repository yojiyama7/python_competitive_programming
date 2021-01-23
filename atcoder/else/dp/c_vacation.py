# 20210123 100%

N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N)]

ABC = [(None, None, None)] + ABC

A, B, C = zip(*ABC)

# i 日目に [海, 山, 家][j] を選んだ時の 幸福度
dp = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(1, N+1):
	dp[i][0] = max(
		dp[i-1][1] + A[i],
		dp[i-1][2] + A[i],
	)
	dp[i][1] = max(
		dp[i-1][0] + B[i],
		dp[i-1][2] + B[i],
	)
	dp[i][2] = max(
		dp[i-1][0] + C[i],
		dp[i-1][1] + C[i],
	)

print(max(dp[N]))
