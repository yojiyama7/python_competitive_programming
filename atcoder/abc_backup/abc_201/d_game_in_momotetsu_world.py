# for 文で書いてみる
# pypyに対して再帰は良くない(学び)

INF = float("inf")

H, W = map(int, input().split())
A = [input() for _ in range(H)]
# H, W = 2000, 2000
# A = [["+-"[(x+y)%2] for x in range(W)] for y in range(H)]

effect = [[1 if c == '+' else -1 for c in line] for line in A]

dp = [[None for _ in range(W)] for _ in range(H)]
dp[H-1][W-1] = (0, 0)
for y in reversed(range(H)):
	for x in reversed(range(W)):
		if x == W-1 and y == H-1:
			continue
		diff = -INF
		if (x+y)%2 == 0:
			# takahashi
			if x+1 < W:
				t, a = dp[y][x+1]
				t += effect[y][x+1]
				if t-a > diff:
					dp[y][x] = (t, a)
					diff = t-a
			if y+1 < H:
				t, a = dp[y+1][x]
				t += effect[y+1][x]
				if t-a > diff:
					dp[y][x] = (t, a)
					diff = t-a
		else:
			# aoki
			if x+1 < W:
				t, a = dp[y][x+1]
				a += effect[y][x+1]
				if a-t > diff:
					dp[y][x] = (t, a)
					diff = a-t
			if y+1 < H:
				t, a = dp[y+1][x]
				a += effect[y+1][x]
				if a-t > diff:
					dp[y][x] = (t, a)
					diff = a-t

t, a = dp[0][0]
# print(t, a)
if t == a:
	print("Draw")
elif t > a:
	print("Takahashi")
else:
	print("Aoki")

################################

# # solve を (x, y) をスタートとした時の点数状況 としてみる

# # TLE

# import sys
# sys.setrecursionlimit(10**8)

# INF = float("inf")

# H, W = map(int, input().split())
# A = [input() for _ in range(H)]
# # H, W = 2000, 2000
# # A = [["+-"[(x+y)%2] for x in range(W)] for y in range(H)]

# effect = [[1 if c == '+' else -1 for c in line] for line in A]

# memo = [[None for _ in range(W)] for _ in range(H)]
# def solve(x, y):
# 	if x == W-1 and y == H-1:
# 		return (0, 0)
# 	if memo[y][x]:
# 		return memo[y][x]
# 	ans = None
# 	diff = -INF
# 	if (x+y)%2 == 0:
# 		# takahashi
# 		if x+1 < W:
# 			t, a = solve(x+1, y)
# 			t += effect[y][x+1]
# 			if t-a > diff:
# 				ans = (t, a)
# 				diff = t-a
# 		if y+1 < H:
# 			t, a = solve(x, y+1)
# 			t += effect[y+1][x]
# 			if t-a > diff:
# 				ans = (t, a)
# 				diff = t-a
# 	else:
# 		# aoki
# 		if x+1 < W:
# 			t, a = solve(x+1, y)
# 			a += effect[y][x+1]
# 			if a-t > diff:
# 				ans = (t, a)
# 				diff = a-t
# 		if y+1 < H:
# 			t, a = solve(x, y+1)
# 			a += effect[y+1][x]
# 			if a-t > diff:
# 				ans = (t, a)
# 				diff = a-t
# 	memo[y][x] = ans
# 	return memo[y][x]

# t, a = solve(0, 0)
# # print(t, a)
# if t == a:
# 	print("Draw")
# elif t > a:
# 	print("Takahashi")
# else:
# 	print("Aoki")

################################

# # 遷移をもう少し詰めた方が良い

# # TLE

# import sys
# sys.setrecursionlimit(10**8)

# INF = float("inf")

# H, W = map(int, input().split())
# A = [input() for _ in range(H)]

# memo = [[None for _ in range(W)] for _ in range(H)]
# # コマが (x, y) にあるときの点数状況
# def solve(x, y):
# 	if x == 0 and y == 0:
# 		return (0, 0)
# 	if memo[y][x]:
# 		return memo[y][x]
# 	ans = None
# 	diff = -INF
# 	if (x+y)%2: # 到着マス
# 		#takahashi
# 		for cx, cy in [(x, y-1), (x-1, y)]:
# 			if not (0 <= cx and 0 <= cy):
# 				continue
# 			t, a = solve(cx, cy)
# 			t += (1 if A[y][x] == '+' else -1)
# 			if a-t > diff:
# 				ans = (t, a)
# 				diff = a-t
# 	else:
# 		# aoki
# 		for cx, cy in [(x, y-1), (x-1, y)]:
# 			if not (0 <= cx and 0 <= cy):
# 				continue
# 			t, a = solve(cx, cy)
# 			a += (1 if A[y][x] == '+' else -1)
# 			if t-a > diff:
# 				ans = (t, a)
# 				diff = t-a
# 	memo[y][x] = ans
# 	return memo[y][x]

# t, a = solve(W-1, H-1)

# # [print(memo_i) for memo_i in memo]

# # print(t, a)
# if t < a:
# 	print("Aoki")
# elif t == a:
# 	print("Draw")
# else:
# 	print("Takahashi")
