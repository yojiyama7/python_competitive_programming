INF = float("inf")

B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]

memo = [None for _ in range(3**9)]
def solve(i, m):
# 	print(i)
# 	print(*m, sep='\n')
	z = 0
	for idx in range(9):
		x, y = idx%3, idx//3
		z *= 3
		z += m[y][x]
	if memo[z]:
		return (memo[z])
	if i == 9:
		t, n = 0, 0
		for y in range(2):
			for x in range(3):
				if m[y][x] == m[y+1][x]:
					t += B[y][x]
				else:
					n += B[y][x]
		for y in range(3):
			for x in range(2):
				if m[y][x] == m[y][x+1]:
					t += C[y][x]
				else:
					n += C[y][x]
		# if (t, n) == (15, 80):
			# print(t, n)
			# print(*m, sep='\n')
		memo[z] = (t, n)
		return memo[z]
	if i%2:
		# naoko
		ans = (-1, -1)
		diff_max = -INF
		for y in range(3):
			for x in range(3):
				if m[y][x] == 0:
					m[y][x] = 2
					t, n = solve(i+1, m)
					m[y][x] = 0
					if diff_max < n - t:
						ans = (t, n)
						diff_max = n - t
		memo[z] = ans
		return (memo[z])
	else:
		# tyokudai
		ans = (-1, -1)
		diff_max = -INF
		for y in range(3):
			for x in range(3):
				if m[y][x] == 0:
					m[y][x] = 1
					t, n = solve(i+1, m)
					m[y][x] = 0
					if diff_max < t - n:
						ans = (t, n)
						diff_max = t - n
		memo[z] = ans
		return (memo[z])

m = [[0 for _ in range(3)] for _ in range(3)]
ans = solve(0, m)
print(*ans, sep='\n')

################################

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