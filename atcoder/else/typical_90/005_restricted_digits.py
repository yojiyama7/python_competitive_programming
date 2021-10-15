# Pypy 速すぎ

MOD = 10**9+7

N, B, K = map(int, input().split())
C = list(map(int, input().split()))

def product(a, b):
	l = [0]*B
	for i, x in enumerate(a):
		for j, y in enumerate(b):
			idx = (i+j) % B
			l[idx] += x*y
			l[idx] %= MOD
	return (l)

def shift_left(a, n):
	l = [0]*B
	p = pow(10, n, B)
	for i, a_i in enumerate(a):
		idx = i*p % B
		l[idx] += a_i
		l[idx] %= MOD
	return (l)

solve_1_ans = [0]*B
for c in C:
	solve_1_ans[c%B] += 1
def solve(n):
	if n == 1:
		return solve_1_ans
	a = solve(n//2)
	b = shift_left(a, n//2)
	l = product(a, b)
	if n%2:
		l = product(shift_left(l, 1), solve(1))
	return l

print(solve(N)[0])
