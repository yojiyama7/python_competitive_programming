# https://atcoder.jp/contests/abc106/tasks/abc106_b

from collections import Counter

N = int(input())

ans = 0
for i in range(1, N+1, 2):
	c = Counter()
	# m = i
	for j in range(2, N+1):
		while i%j == 0:
			c[j] += 1
			i //= j
	d = 1
	for v in c.values():
		d *= v+1
	if d == 8:
		ans += 1
		# print(m, c)

print(ans)
