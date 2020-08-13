import numpy as np

S = input()

dp = np.zeros((len(S)+1, 13), np.int64)
dp[0][0] = 1

for s in S:
    if s == "?":

################################
# # PyPy AC
# # Python3 TLE

# S = input()

# # 下からi桁(1-indexed)まで使ったときの、13で割ったときあまりがjになるパターン
# dp = [[0 for _ in range(13)] for _ in range(len(S)+1)]
# dp[0][0] = 1

# for i, s in enumerate(S[::-1]):
#     r_now = [1, 10, 9, 12, 3, 4][i%6]
#     if s == "?":
#         for d in range(10):
#             for r_before, count in enumerate(dp[i]):
#                 j = (r_now*d+r_before)%13
#                 dp[i+1][j] = (dp[i+1][j]+count)%(10**9+7)
#     else:
#         d = int(s)
#         for r_before, count in enumerate(dp[i]):
#             j = (r_now*d+r_before)%13
#             dp[i+1][j] = (dp[i+1][j]+count)%(10**9+7)
#     # for dp_i in dp:
#     #     print(dp_i)
#     # print("")

# print(dp[len(S)][5])