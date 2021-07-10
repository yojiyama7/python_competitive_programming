INF = float('inf')

N = int(input())
APX = [list(map(int, input().split())) for _ in range(N)]

min_num = INF
for a, p, x in APX:
	if a < x:
		min_num = min(min_num, p)

print(-1 if min_num == INF else min_num)
