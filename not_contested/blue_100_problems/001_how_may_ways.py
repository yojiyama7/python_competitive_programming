# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja

while True:
	N, X = map(int, input().split())
	if N == X == 0:
		break
	ans = 0
	for a in range(1, N+1):
		for b in range(a+1, N+1):
			for c in range(b+1, N+1):
				if a+b+c == X:
					ans += 1
	print(ans)
