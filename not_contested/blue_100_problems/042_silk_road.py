# https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d

INF = float('inf')

N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

D = [None] + D
C = [None] + C

# dp[i][j]: i日目の都市j到達時の最小スコア
dp = [[INF for j in range(N+1)] for i in range(M+1)]
for i in range(M+1):
    dp[i][0] = 0

for i in range(1, M+1):
    c = C[i]
    for j in range(1, N+1):
        d = D[j]
        dp[i][j] = min(
            dp[i-1][j-1] + c*d,
            dp[i-1][j],
        )

# list(map(print, dp))

print(dp[M][N])
