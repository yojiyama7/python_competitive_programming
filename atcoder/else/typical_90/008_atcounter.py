# dp センスが高まってきている気がする

MOD = 10**9+7

N = int(input())
S = input()

S = "_" + S

# i(1idx)文字目までで "atcoder"[:j] を部分文字列として作れるパターン数
dp = [[0]*8 for _ in range(N+1)]
dp[0][0] = 1
# print(dp[0])
for i in range(1, N+1):
	# print(S[1:i+1])
	for j in range(8):
		dp[i][j] = dp[i-1][j]
		if j-1 >= 0 and S[i] == "atcoder"[j-1]:
			# print([i, j])
			dp[i][j] += dp[i-1][j-1]
		dp[i][j] %= MOD
	# print(dp[i])

# [print(dp_i) for dp_i in dp]

print(dp[N][7])
