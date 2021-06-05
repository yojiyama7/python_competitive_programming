# https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b

INF = float('inf')

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = INF
for i in range(1<<N):
	cost = 0
	cnt = 0
	before = 0
	for j in range(N):
		t = A[j]
		if (i>>j)&1:
			cnt += 1
			if (before + 1) >= A[j]:
				cost += (before + 1) - A[j]
				t = (before + 1)
		before = max(t, before)
	if cnt >= K:
		ans = min(cost, ans)

print(ans)
