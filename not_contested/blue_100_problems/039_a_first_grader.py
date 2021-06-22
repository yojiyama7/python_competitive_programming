# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d

# より難しい問題に誤読した

N = int(input())
A = list(map(int, input().split()))

dp = [[0 for j in range(21)] for i in range(N-1)]

dp[0][A[0]] = 1
for i in range(1, N-1):
    for j in range(21):
        if j-A[i] >= 0:
            dp[i][j] += dp[i-1][j-A[i]]
        if j+A[i] <= 20:
            dp[i][j] += dp[i-1][j+A[i]]

print(dp[N-2][A[N-1]])

################################

# N = int(input())
# A = list(map(int, input().split()))

# # dp[i][j][k]: [i, j] の範囲で k を何通り作れるか
# dp = [[[0 for k in range(21)] for j in range(N)] for i in range(N)]

# for i in range(N):
#     dp[i][i][A[i]] = 1

# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(21):
#             if k-A[j] >= 0:
#                 dp[i][j][k] += dp[i][j-1][k-A[j]]
#             if k+A[j] <= 20:
#                 dp[i][j][k] += dp[i][j-1][k+A[j]]

# for dp_i in dp:
#     print(*dp_i, sep='\n')
#     print()

# ans = 0
# for i in range(N-1):
#     for k in range(21):
#         ans += dp[0][i][k] * dp[i+1][N-1][k]
# print(ans)

################################

# N = int(input())
# A = list(map(int, input().split()))

# dp1 = [[0 for _ in range(21)] for _ in range(N)]
# dp1[0][A[0]] = 1
# for i in range(1, N):
#     Ai = A[i]
#     for j in range(21):
#         if j-Ai >= 0:
#             dp1[i][j] += dp1[i-1][j-Ai]
#         if j+Ai <= 20:
#             dp1[i][j] += dp1[i-1][j+Ai]

# dp2 = [[0 for _ in range(21)] for _ in range(N)]
# dp2[N-1][A[N-1]] = 1
# for i in reversed(range(N-1)):
#     Ai = A[i]
#     for j in range(21):
#         if j-Ai >= 0:
#             dp2[i][j] += dp2[i+1][j-Ai]
#         if j+Ai <= 20:
#             dp2[i][j] += dp2[i+1][j+Ai]

# print(*dp1, sep='\n')
# print(*dp2, sep='\n')

# ans = 0
# for i in range(N-1):
#     for j in range(21):
#         ans += dp1[i][j]*dp2[i+1][j]

# print(ans)