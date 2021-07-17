INF = float('inf')

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# dp[i][j][flag]: flag == 1 なら 2個, == 0 なら 1個の駅を立てて　(i, j)<y, x> にたどり着く時 最小コストは？
# ただし 左->右, 上->下のみの移動とする
dp = [[[A[i][j], INF] for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        # (i, j) に 2 個目の駅を立てない
        for flag in range(2):
            if i-1 >= 0:
                dp[i][j][flag] = min(
                    dp[i-1][j][flag] + C,
                    dp[i][j][flag]
                )
            if j-1 >= 0:
                dp[i][j][flag] = min(
                    dp[i][j-1][flag] + C,
                    dp[i][j][flag]
                )
        # 立てる
        if i-1 >= 0:
            dp[i][j][1] = min(
                dp[i-1][j][0] + C + A[i][j],
                dp[i][j][1]
            )
        if j-1 >= 0:
            dp[i][j][1] = min(
                dp[i][j-1][0] + C + A[i][j],
                dp[i][j][1]
            )

ans = INF
for dp_i in dp:
    for dp_ij in dp_i:
        ans = min(ans, dp_ij[1])

# ただし **右->左**, 上->下のみの移動とする
dp = [[[A[i][j], INF] for j in range(W)] for i in range(H)]
for i in range(H):
    for j in reversed(range(W)):
        # (i, j) に 2 個目の駅を立てない
        for flag in range(2):
            if i-1 >= 0:
                dp[i][j][flag] = min(
                    dp[i-1][j][flag] + C,
                    dp[i][j][flag]
                )
            if j+1 < W:
                dp[i][j][flag] = min(
                    dp[i][j+1][flag] + C,
                    dp[i][j][flag]
                )
        # 立てる
        if i-1 >= 0:
            dp[i][j][1] = min(
                dp[i-1][j][0] + C + A[i][j],
                dp[i][j][1]
            )
        if j+1 < W:
            dp[i][j][1] = min(
                dp[i][j+1][0] + C + A[i][j],
                dp[i][j][1]
            )

for dp_i in dp:
    for dp_ij in dp_i:
        ans = min(ans, dp_ij[1])

print(ans)
