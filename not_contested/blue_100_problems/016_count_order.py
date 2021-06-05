# https://atcoder.jp/contests/abc150/tasks/abc150_c

from itertools import permutations as permu

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

r = list(permu(range(1, N+1)))
r.sort()

a, b = None, None
for i, l in enumerate(r):
	if l == P:
		a = i
	if l == Q:
		b = i

print(abs(a-b))
