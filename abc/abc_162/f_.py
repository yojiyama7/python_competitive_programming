# DP

# N = int(input())
# A = list(map(int, input().split()))

# a = [0] + A + [0]*10

# jump_limit = N%2 + 1
# # dp[i][j] = i番目まででjマスjumpをして、
# # できる和の最大数
# dp = [[-(10**18) for _ in range(jump_limit+1)] for _ in range(N+10)]
# for i in range(jump_limit+1):
#     dp[0][i] = 0
# dp[1][0] = a[1]
# for i in range(1, N+1):
#     for j in range(jump_limit+1):
#         dp[i+2][j] = max(
#             dp[i][j] + a[i+2],
#             dp[i+2][j]
#         )
#         if j >= 1:
#             dp[i+3][j] = max(
#                 dp[i][j-1] + a[i+3],
#                 dp[i+3][j]
#             )
#         if j >= 2:
#             dp[i+4][j] = max(
#                 dp[i][j-2] + a[i+4],
#                 dp[i+4][j]
#             )

# print(dp)
# print(dp[N][jump_limit])