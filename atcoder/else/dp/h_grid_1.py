# 20210123 100%

MOD = 10**9 + 7

H, W = map(int, input().split())
A = [input() for _ in range(H)]

A = ["_"*(W+1)] + ["_"+a for a in A]

# dp[i][j]: (i, j) でのパターン数(mod 10**9 + 7)

dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
dp[1][1] = 1
for y in range(1, H+1):
	for x in range(1, W+1):
		if x == y == 1:
			continue
		if A[y][x] == "#":
			continue
		dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD

# print(*dp, sep="\n")
print(dp[H][W])
