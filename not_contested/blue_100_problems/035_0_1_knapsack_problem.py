# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja

N, W = map(int, input().split())
VW = [list(map(int, input().split())) for _ in range(N)]
# N, W = 100, 10000
# VW = [[i, 1] for i in range(N)]

VW = [None] + VW

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(1, N+1):
    v, w = VW[i]
    for j in range(W+1):
        if j-w >= 0:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-w] + v
            )
        else:
            dp[i][j] = dp[i-1][j]

# list(map(print, dp))

print(dp[N][W])
