# python3 TLE
# PyPy3 AC

N, W = map(int, input().split(" "))
WV = [list(map(int, input().split(" "))) for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i, (w, v) in enumerate(WV):
    for j in range(W+1):
        if w <= j:
            dp[i+1][j] = max(
                dp[i][j-w] + v,
                dp[i][j]
            )
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])

################################

# # TLE

# import sys

# sys.setrecursionlimit(10**8)

# N, W = map(int, input().split(" "))
# WV = [list(map(int, input().split(" "))) for _ in range(N)]
# # N, W = 100, 10**5
# # WV = [[i*190, 10] for i in range(N)]


# l = [[None for _ in range(W+1)] for _ in range(N+1)]
# def dp(i, limit):
#     if i == -1:
#         return 0
#     if l[i][limit] != None:
#         return l[i][limit]
#     w, v = WV[i]
#     if w <= limit:
#         l[i][limit] = max(
#             dp(i-1, limit),
#             dp(i-1, limit-w) + v
#         )
#     else:
#         l[i][limit] = dp(i-1, limit)
#     return l[i][limit]

# print(dp(N-1, W))
