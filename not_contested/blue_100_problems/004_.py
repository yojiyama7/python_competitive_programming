# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c

from itertools import combinations as combi

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
for a, b in combi(range(M), 2):
	score = 0
	for i in range(N):
		score += max(A[i][a], A[i][b])
	max_num = max(score, max_num)

print(max_num)
