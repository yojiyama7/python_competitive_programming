# 0-indexed と 1-indexed どちらがいいんでしょうかの気持ち

INF = float('inf')

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[INF for _ in range(W)] for _ in range(H)]
dp[0][0] = (S[0][0] == "#")
for y in range(H):
    for x in range(W):
        if x-1 >= 0:
            cost = (S[y][x-1] == "." and S[y][x] == "#")
            dp[y][x] = dp[y][x-1] + cost
        if y-1 >= 0:
            cost = (S[y-1][x] == "." and S[y][x] == "#")
            dp[y][x] = min(
                dp[y][x],
                dp[y-1][x] + cost
            )

print(dp[H-1][W-1])