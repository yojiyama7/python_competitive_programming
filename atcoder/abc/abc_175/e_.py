# やはりDPは苦手

# R, C: H, W

H, W, K = map(int, input().split())
YXV = [list(map(int, input().split())) for _ in range(K)]

# H, W, K = 3000, 3000, 2*10**5
# YXV = [(i//H, i%W, i) for i in range(K)]

# H, W, K = 2, 2, 4
# YXV = [(1+i//H, 1+i%W, 1+i) for i in range(K)]

item = [[0 for _ in range(W+2)] for _ in range(H+2)]
for y, x, v in YXV:
    item[y][x] = v

# [print(item_i) for item_i in item]

dp = [[[0]*4 for _ in range(W+2)] for _ in range(H+2)]
dp[1][1][1] = item[1][1] 
for ty in range(1, H+1):
    for tx in range(1, W+1):
        # アイテムを拾わない
        # print(f"pos: ({tx}, {ty})", end="\r")
        dp[ty+1][tx][0] = max(
            dp[ty+1][tx][0],
            dp[ty][tx][3]
        )
        for k in range(4):
            dp[ty][tx+1][k] = max(
                dp[ty][tx+1][k],
                dp[ty][tx][k]
            )
        # print((x, y), item[y][x])
        if item[ty][tx] == 0:
            continue
        # アイテムを拾う
        for k in range(4):
            dp[ty+1][tx][0] = max(
                dp[ty+1][tx][0],
                dp[ty][tx][k] + item[ty+1][tx]
            )
        for k in range(3):
            dp[ty][tx+1][k+1] = max(
                dp[ty][tx+1][k+1],
                dp[ty][tx][k] + item[ty][tx+1]
            )

# for dp_i in dp:
#     print(dp_i)

print(max(dp[H][W]))