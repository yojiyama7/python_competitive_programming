# https://atcoder.jp/contests/abc128/tasks/abc128_c

N, M = map(int, input().split())
KS = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

S = [s for _, *s in KS]

ans = 0
for i in range(1<<N):
	flag = 1
	for j, s in enumerate(S):
		if sum((i>>(x-1))&1 for x in s) % 2 == P[j]:
			continue
		flag = 0
		break
	if flag:
		ans += 1
print(ans)
