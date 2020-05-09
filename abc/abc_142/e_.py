N, M = map(int, input().split())
AB_C = [[list(map(int, input().split())) for _ in range(2)] for _ in range(M)]

keys = []
for i, ((a, b), c) in enumerate(AB_C):
    key_flag = 0
    for c_i in c:
        key_flag |= 1<<(c_i-1)
    keys.append((a, key_flag))

dp = [[10**18 for _ in range(1<<N)] for _ in range(M+1)]
dp[0][0] = 0

for i, (price, flag) in enumerate(keys):
    for j in range(1<<N):
        dp[i+1][j] = min(
            dp[i+1][j],
            dp[i][j]
        )
        dp[i+1][j|flag] = min(
            dp[i+1][j|flag],
            dp[i+1][j] + price
        )

r = dp[M][(1<<N)-1]
print(-1 if r == 10**18 else r)

################################

# # うーん精進不足だ集中してやろう。

# N, M = map(int, input().split())
# AB_C = [[list(map(int, input().split())) for _ in range(2)] for _ in range(M)]

# # i番目までの鍵でjの状態にする最少額
# DP = [[10**18 for _ in range(1<<N)] for _ in range(M+1)]
# DP[0][0] = 0

# for i in range(M):
#     (a, b), c = AB_C[i]
#     f = 0
#     for c_i in c:
#         f |= 1<<(c_i-1)
#     # print(a, b, c, bin(f))
#     for j in range(1<<N):
#         # print(i, j, f, a, DP[i][j|f], DP[i][j] + a, min(DP[i][j|f], DP[i][j] + a))
#         DP[i+1][j|f] = min(
#             DP[i+1][j|f],
#             DP[i][j|f],
#             DP[i][j] + a
#         )
#         # print(i+1, j|f, DP[i+1][j|f])
#     # print(DP)

# # print(DP)
# r = DP[M][(1<<N)-1]
# print(-1 if r == 10**18 else r)