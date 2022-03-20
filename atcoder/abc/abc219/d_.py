INF = 10**18

N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [[[INF for k in range(Y+1)] for j in range(X+1)] for i in range(N+1)]
dp[0][0][0] = 0

for i, (a, b) in enumerate(AB):
    for j in range(X+1):
        for k in range(Y+1):
            dp[i+1][j][k] = min(
                dp[i+1][j][k],
                dp[i][j][k]
            )
            c, d = min(X, j+a), min(Y, k+b)
            dp[i+1][c][d] = min(
                dp[i+1][c][d],
                dp[i][j][k] + 1
            )

ans = -1 if dp[N][X][Y] == INF else dp[N][X][Y]
print(ans)
