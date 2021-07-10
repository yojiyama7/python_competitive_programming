
################################

# COMMENT: numpyを覚えてください。

# TLE

# R, C: Y, H
# H, W, K = map(int, input().split())
# RCV = [list(map(int, input().split())) for _ in range(K)]
H, W, K = 3000, 3000, 2*10**5
RCV = [[i//W, i%W, i] for i in range(K)]

item = [[0]*(W+1) for _ in range(H+1)]
for r, c, v in RCV:
    item[r][c] = v
# for item_i in item:
#     print(item_i)

dp = [[[0]*4 for _ in range(W+1)] for _ in range(H+1)]

# 3000**2*4*2 + 2*10**5*2*4
for y in range(1, H+1):
    print(y, "   ", end="\r")
    for x in range(1, W+1):
        for k in range(4):
            dp[y][x][0] = max(
                dp[y][x][0],
                dp[y-1][x][k],
            )
            dp[y][x][1] = max(
                dp[y][x][1],
                dp[y-1][x][k] + item[y][x],
            )
            dp[y][x][k] = max(
                dp[y][x][k],
                dp[y][x-1][k],
            )
        for k in range(1, 4):
            # dp[y][x][k] = max(
            #     dp[y][x][k],
            #     dp[y][x-1][k],
            # )
            # if k == 0:
            #     continue
            dp[y][x][k] = max(
                dp[y][x][k],
                dp[y][x-1][k-1] + item[y][x]
            )
# for dp_i in dp:
#     print(dp_i)

print(max(dp[H][W]))

################################

# # WA

# # R, C: H, W

# H, W, K = map(int, input().split())
# # YXV = [list(map(int, input().split())) for _ in range(K)]
# # H, W, K = 3000, 3000, 2*10**5
# # YXV = [(i//H, i%W, i) for i in range(K)]

# item = [[0 for _ in range(W+2)] for _ in range(H+2)]
# for _ in range(K):
#     y, x, v = map(int, input().split())
#     item[y][x] = v

# # [print(item_i) for item_i in item]

# dp = [[[0]*4 for _ in range(W+2)] for _ in range(H+2)]
# dp[1][1][1] = item[1][1] 
# for ty in range(1, H+1):
#     for tx in range(1, W+1):
#         # アイテムを拾わない
#         # print(f"pos: ({tx}, {ty})", end="\r")
#         for k in range(4):
#             dp[ty+1][tx][0] = max(
#                 dp[ty+1][tx][0],
#                 dp[ty][tx][k]
#             )
#             dp[ty][tx+1][k] = max(
#                 dp[ty][tx+1][k],
#                 dp[ty][tx][k]
#             )
#         # print((x, y), item[y][x])
#         if item[ty][tx] == 0:
#             continue
#         # アイテムを拾う
#         for k in range(4):
#             dp[ty+1][tx][0] = max(
#                 dp[ty+1][tx][0],
#                 dp[ty][tx][k] + item[ty+1][tx]
#             )
#         for k in range(3):
#             dp[ty][tx+1][k+1] = max(
#                 dp[ty][tx+1][k+1],
#                 dp[ty][tx][k] + item[ty][tx+1]
#             )

# # for dp_i in dp:
# #     print(dp_i)

# print(max(dp[H][W]))
