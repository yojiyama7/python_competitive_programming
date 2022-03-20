from itertools import accumulate as acc

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

board = [[0 for _ in range(1001)] for _ in range(1001)]
for a, b, x, y in LR:
    board[a][b] += 1
    board[a][y] -= 1
    board[x][b] -= 1
    board[x][y] += 1

# def acc_vec2(h, w, board):
#     def f(a, b):
#         res = [0]*(w+1)
#         for i, (ai, bi) in enumerate(zip(a, b)):
#             res[i] = ai+bi
#         return res
#     tmp = [[0] + list(acc(bi)) for bi in board]
#     res = [[0 for _ in range(w+1)]] + list(acc(tmp, func=f))
#     return res

dp = [[0 for _ in range(1002)] for _ in range(1002)]
for i in range(1001):
    for j in range(1001):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + board[i][j]

ans = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        ans[dp[i][j]] += 1

print(*ans[1:], sep='\n')
