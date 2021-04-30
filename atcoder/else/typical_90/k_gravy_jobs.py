N = int(input())
DCS = [list(map(int, input().split())) for _ in range(N)]

# これでうまくいくことが証明できません
# お気持ちだけでも知りたい
DCS.sort()
DCS = [None] + DCS

days = 5000

# i番目までの仕事でj日目に達成できる最大スコア
dp = [[0]*(days+1) for _ in range(N+1)]
for i in range(1, N+1):
	d, c, s = DCS[i]
	for j in range(1, days+1):
		dp[i][j] = max(
			dp[i-1][j],
			dp[i][j-1]
		)
		if c <= j <= d:
			dp[i][j] = max(
				dp[i-1][j-c] + s,
				dp[i][j]
			)
# [print(dp_i) for dp_i in dp]
print(dp[N][days])