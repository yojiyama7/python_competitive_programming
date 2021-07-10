# from icecream import ic

# dp の項目がN個、それぞれの更新にO(M)かかって合計O(NM) となるような一次元dp がある

INF = float('inf')

H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [INF for _ in range(H+1)]
dp[0] = 0
for i in range(H):
    for a, b in AB:
        # ic(dp[min(H, i+a)], dp[i] + b)
        dp[min(H, i+a)] = min(
            dp[min(H, i+a)],
            dp[i] + b
        )

# print(dp)
print(dp[H])


################################

# 1次元でいいってま？

# INF = float('inf')

# H, N = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]

# AB = [None] + AB

# # dp[i][j] = i番目まででjダメージを与えるときの最小
# dp = [[INF for j in range(H+1)] for _ in range(N+1)]
# dp[0][0] = 0
# for i in range(1, N+1):
#     a, b = AB[i]
#     for j in range(H+1):
#         if j-a >= 0:
#             dp[i][j] = min(
#                 dp[i-1][j-a] + b,
#                 dp[i][j-a] + b
#             )

################################
# # 個数制限なしDP yannke 

# H, N = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(N)]

# # i番目までの魔法でjダメージを与えるために必要な最小魔力
# dp = [[10**18 for j in range(H+10**4+1)] for i in range(N+1)]
# dp[0][0] = 0
# for i in range(1, N+1):
#     a, b = AB[i-1]
#     for j in range(H+1):
#         if j-a >= 0:
#             dp[i][j] = min(
#                 dp[i-1][j],
#                 dp[i-1][j-a] + b
#             )
#         else:
#             dp[i][j] = dp[i-1][j]

# [print(dp_i[:10]) for dp_i in dp]
# print(min(dp[N][H:]))