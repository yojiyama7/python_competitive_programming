H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sum = list(map(sum, A))
col_sum = list(map(sum, zip(*A)))

for y in range(H):
	l = [col_sum[x] + row_sum[y] - A[y][x] for x in range(W)]
	print(*l)
