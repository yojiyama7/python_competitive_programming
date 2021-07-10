# from icecream import ic
# print = ic

from itertools import accumulate as acc

N, K = map(int, input().split())

idx = K-1

# K番目のケーキのスコアの算出 dp
# i(0~3)個選んでj(3~3N)を作る通り数
dp = [[0 for _ in range(3*N+1)] for _ in range(3+1)]
dp[0][0] = 1
for i in range(1, 3+1):
	dp_before_acc = [0] + list(acc(dp[i-1]))
	for j in range(3*N+1):
		dp[i][j] += dp_before_acc[j] - dp_before_acc[max(0, j-N)]

score = None
for i, cnt in enumerate(dp[3]):
	# print(i, idx, end='\r')
	if idx < cnt:
		score = i
		break
	idx -= cnt

# print(score)

for a in range(1, N+1):
	# print(a, idx)
	remain = score-a
	b_min = max(1, remain-N)
	b_max = min(N, remain-1)
	if b_min > b_max:
		continue
	cnt = b_max-b_min+1
	# print(cnt)
	if idx < cnt:
		b = b_min + idx
		c = score-a-b
		if not (1 <= c <= N):
			continue
		print(a, b, c)
		break
	idx -= cnt

#################################

# N, K = map(int, input().split())

# idx = K-1

# score = None
# before = 0
# for i in range(3, 3*N+1):
# 	cnt = (i-1)*(i-2)//2
# 	if idx < before + cnt:
# 		score = i
# 		break
# 	before += cnt

# idx -= before
# print(score, idx, before)

# # print(score)
# a = None
# before = 0
# for i in range(1, N+1):
# 	if not (2 <= score - i <= 2*N):
# 		continue
# 	# ここわからん
# 	cnt = (2*N-2) - (score - i - 2)
# 	if idx < before + cnt:
# 		a = i
# 		break
# 	before += cnt

# idx -= before
# print(a, idx, before)

# b = None
# before = 0
# for i in range(1, N-a+1):
# 	# ここわからん
# 	cnt = 1
# 	if idx < before + cnt:
# 		b = i
# 		break
# 	before += cnt

# idx -= before
# print(b, idx, before)

# c = score - a - b

# print(a, b, c)

################################

# N, K = map(int, input().split())

# # 3つの総和をスコアとする
# # K 番目のスコアが何であるか求める
# # 各スコアに属すパターンはたかだか3*10**6 程度しかないので
# # 全探索

# score = None
# before = 0
# for i in range(3, 3*N+1):
# 	cnt = (i-1)*(i-2)//2
# 	if K <= before + cnt:
# 		score = i
# 		break
# 	before += cnt

# print(K, before, K, before + cnt)
# # ここの-1は b_cnt <= K−1 < cnt という形式にして 0-indexed 的にしたいから
# # x は 0-indexed で スコアが score のものの中で 何番目のものを求めるべきか という数
# # x はたかだか 2999998 である
# x = K-1 - before
# # l は答えの形式とは逆順である
# l = [1, 1, 1]
# for i in range(score-3):
# 	for j in range(3):
# 		if l[j] < N:
# 			l[j] += 1
# 			break

# print(x)
# for i in range(x):
# 	a = None
# 	b = None
# 	for j in range(3):
# 		if l[j] > 1:
# 			a = j
# 			break
# 	for j in range(3):
# 		if l[j] <= N and a:
# 			b = j
# 			break
# 	print(score, l, a, b)
# 	l[a] -= 1
# 	l[b] += 1

# print(*l[::-1])