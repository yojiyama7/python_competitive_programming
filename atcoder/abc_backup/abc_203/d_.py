# 定数倍くそ 二次元累積和はテンプレ用意した方が良さそう
# 誤読と定数倍に殺されかけた
# でも詰めの甘さはしっかりカバーした これはよかった
# 誤読, 詰甘, 定数倍 は意識した方が良い

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# N, K = 800, 400
# A = [[100]*N]*N

# 偶数の時の中央値は大きい方 奇数の時は真ん中

limit = (K**2)//2 + 1
# print((K, K**2, limit, (K**2-limit)))

def is_ok(mid):
	# print(">>>", mid)
	# O(N**2) * 4
	b = [[m > mid for m in line] for line in A]
	b_acc = [[0 for _ in range(N+1)] for _ in range(N+1)]
	for y in range(1, N+1):
		for x in range(1, N+1):
			b_acc[y][x] = b_acc[y][x-1] + b[y-1][x-1]
	for y in range(1, N+1):
		for x in range(1, N+1):
			b_acc[y][x] += b_acc[y-1][x]
	# b_acc = [[0] + list(acc(b_i)) for b_i in b]
	# b_acc = [[0] + list(acc(b_i)) for b_i in zip(*b_acc)]
	# b_acc = list(zip(*b_acc))
	# [print(line) for line in b]
	# [print(line) for line in b_acc]
	# O(N**2)
	for y in range(N-K+1):
		for x in range(N-K+1):
			score = b_acc[y+K][x+K] - b_acc[y+K][x] - b_acc[y][x+K] + b_acc[y][x]
			if score < limit:
				# print([x, y], score)
				return True
	return False

# O(log (10**9)) < 30
ok, ng = 10**9, -1
while abs(ok - ng) > 1:
	mid = (ok+ng)//2
	if is_ok(mid):
		ok = mid
	else:
		ng = mid

print(ok)
