MOD = 998244353

A, B, C, D = map(int, input().split())

dp = [[0 for _ in range(D+1)] for _ in range(C+1)]
dp[A][B] = 1

for i in range(A+1, C+1):
    dp[i][B] = dp[i-1][B] * B
for j in range(B+1, D+1):
    dp[A][j] = dp[A][j-1] * A

for i in range(A+1, C+1):
    for j in range(B+1, D+1):
        up = dp[i-1][j]
        left = dp[i][j-1]
        dp[i][j] += (up*left) % MOD
        dp[i][j] += (up + left) % MOD
        dp[i][j] %= MOD

print(*dp, sep='\n')

print(dp[C][D])