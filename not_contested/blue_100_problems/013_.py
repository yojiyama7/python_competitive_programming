# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e

R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

max_num = 0
for i in range(1<<R):
	score = 0
	for x in range(C):
		cnt = 0
		for y in range(R):
			cnt += (A[y][x] + ((i>>y)&1))%2
		score += max(cnt, R-cnt)
	max_num = max(score, max_num)

print(max_num)
