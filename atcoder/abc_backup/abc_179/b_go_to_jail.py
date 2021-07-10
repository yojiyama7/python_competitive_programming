N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

l = [a == b for a, b in D]

cnt = 0
max_cnt = 0
for l_i in l:
	if l_i == 0:
		max_cnt = max(max_cnt, cnt)
		cnt = 0
	else:
		cnt += 1
max_cnt = max(max_cnt, cnt)

print("Yes" if max_cnt >= 3 else "No")