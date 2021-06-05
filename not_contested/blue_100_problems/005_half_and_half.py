# https://atcoder.jp/contests/abc095/tasks/arc096_a

INF = float('inf')

A, B, C, X, Y = map(int, input().split())

min_num = INF
for common in range(max(X, Y)*2 +1):
	cost = C * common
	cost += A * max(X-common//2, 0)
	cost += B * max(Y-common//2, 0)
	min_num = min(min_num, cost)

print(min_num)
