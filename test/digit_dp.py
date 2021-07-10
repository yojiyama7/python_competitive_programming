# N = 1000
# S = str(N)

# memo = dict()
# def solve(x, sm):
#     if memo[(x, sm)]:
#         return memo[(x, sm)]
#     if sm == 0:
#         return solve(x//10, 0)
#     else:
#         solve(x//10, 1) * 10 + solve(x//10, 0) * l[] 

################################

# N = 1000
# S = str(N)

# # N 以下の整数の個数を求めよ

# l = [None] + list(map(int, S))
# S_len = len(S)

# # dp[i][sm]: i桁目までのスコア
# dp = [[0 for sm in range(2)] for i in range(S_len+1)]
# dp[0][0] = 1

# # N の i 桁目までの整数について考える

# for i in range(1, S_len+1):
#     dp[i][0] += dp[i-1][0]
#     dp[i][1] += dp[i-1][1]*10 + dp[i-1][0]*l[i]

# print(dp)

