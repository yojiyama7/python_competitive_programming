# 惜しい。遅い。

# B = [list(map(int, input().split())) for _ in range(2)]
# C = [list(map(int, input().split())) for _ in range(3)]

# # score = chokudai_score - naoko_score
# # chokudai: scoreの最"大"化
# # naoko   : scoreの最"小"化
# dp = [None for i in range(3**9)]
# def solve_score(m):
#     dp_id = 0
#     for i, m_i in enumerate(m):
#         for j, m_j in enumerate(m_i):
#             if m_j == 0:
#                 dp_id += 3**(i*3+j)
#             elif m_j == 1:
#                 dp_id += 3**(i*3+j) * 2
#     if dp[dp_id] == None:
#         c_score, n_score = 0, 0
#         for i in range(2):
#             for j in range(3):
#                 if -1 in [m[i][j], m[i+1][j]]:
#                     continue
#                 elif m[i][j] == m[i+1][j]:
#                     c_score += B[i][j]
#                 else:
#                     n_score += B[i][j]
#         for i in range(3):
#             for j in range(2):
#                 if -1 in [m[i][j], m[i][j+1]]:
#                     continue
#                 elif m[i][j] == m[i][j+1]:
#                     c_score += C[i][j]
#                 else:
#                     n_score += C[i][j]
#         dp[dp_id] = (c_score, n_score)
#     return dp[dp_id]
# # player_sign: {0: chokudai, 1: naoko} (left_turn % 2)
# def bfs(m, left_turn=0):
#     m_c_score, m_n_score = solve_score(m)
#     if left_turn == 9:
#         return (m_c_score, m_n_score)
#     player = left_turn%2
#     best_score = [-(10**18), 10**18][::[1, -1][player]]
#     for y in range(3):
#         for x in range(3):
#             if m[y][x] >= 0:
#                 continue
#             m[y][x] = player
#             score = bfs(m, left_turn=left_turn+1)
#             # score = 0, 0
#             f = [max, min][player]
#             best_score = f([best_score, score], key=lambda nc: nc[0]-nc[1])
#             m[y][x] = -1
#     return best_score

# score = bfs([[-1]*3 for _ in range(3)], 0)
# [print(s) for s in score]

################################

# from itertools import chain

# B = [list(map(int, input().split(" "))) for _ in range(2)]
# C = [list(map(int, input().split(" "))) for _ in range(3)]

# def p(m):
#     if 0 not in chain(m):
#         score = 0
#         for i in range(2):
#             for j in range(3):
#                 if m[i][j] == 0 and m[i][j] == m[i+1][j]:
#                     score += B[i][j]
#         for i in range(3):
#             for j in range(2):
#                 if m[i][j] == 0 and m[i][j] == m[i][j+1]:
#                     score += C[i][j]
#         return score

################################

# ゲーム木全探索
# B = [list(map(int, input().split(" "))) for _ in range(2)]
# C = [list(map(int, input().split(" "))) for _ in range(3)]

# def dfs(m):
#     pass