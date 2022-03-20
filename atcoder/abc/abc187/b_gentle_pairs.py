N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
	for j in range(i+1, N):
		x0, y0 = XY[i]
		x1, y1 = XY[j]
		w = x1-x0
		h = y1-y0
		if -1 <= h/w <= 1:
			cnt += 1

print(cnt)
