# https://atcoder.jp/contests/abc023/tasks/abc023_d

N = int(input())
HS = [list(map(int, input().split())) for _ in range(N)]

ok, ng = 10**20, 0
while abs(ok-ng) > 1:
	mid = (ok+ng)//2
	# 全ての風船を mid 以下の高さで割れるなら
	# >>> スコアが mid 以下にできるなら
	# 各風船　i に対して 遅くとも time_limit[i] 番目に処理しないといけない
	# time_limit[i] = (mid - H[i])//S[i]
	# [0, 0, 1, 2] -> ok
	# [0, 1, 2, 3] -> ok
	# [0, 1, 3, 4] -> ng
	time_limit = [(mid - h)//s  for h, s in HS]
	time_limit.sort()
	# print(ok, mid, ng, time_limit)
	if all(l >= t for l, t in zip(time_limit, range(N))):
		ok = mid
	else:
		ng = mid

print(ok)
