

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