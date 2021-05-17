N = int(input())
A = list(map(int, input().split()))

A = [None] + A

# 最大2パターン記録する
pattern = [[set() for j in range(200)] for i in range(N+1)]
pattern[0][0].add(tuple())
dp = [[0 for j in range(200)] for i in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
	a = A[i]
	for j in range(200):
		dp[i][j] += dp[i-1][j]
		dp[i][j] += dp[i-1][(j-a)%200]
		# if dp[i][j] >= 2:
		# 	print((i, j), pattern[i][j])
		if dp[i-1][j] and len(pattern[i][j]) < 2:
			pattern[i][j] |= pattern[i-1][j]
		if dp[i-1][(j-a)%200] and len(pattern[i][j]) < 2:
			for x in pattern[i-1][(j-a)%200]:
				l = tuple(list(x) + [i])
				pattern[i][j].add(l)
		if len(pattern[i][j]) > 2:
			pattern[i][j] = set(list(pattern[i][j])[:2])

# for i in range(200):
# 	print(i, dp[N][i], pattern[N][i])
# mod200において Bのスコア == Cのスコア になるとき
# そのスコアは何になるのかはわかっている
# そのスコアがわかっていれば復元できるか？

for j, x in enumerate(dp[N]):
	if j == 0:
		continue
	if x >= 2:
		print("Yes")
		# print(list(pattern[N][j]))
		a, b = list(pattern[N][j])
		print(len(a), *a)
		print(len(b), *b)
		exit()
print("No")
