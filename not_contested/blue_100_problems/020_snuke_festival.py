# https://atcoder.jp/contests/abc077/tasks/arc084_a

from bisect import bisect_left, bisect_right

N = int(input())
A, B, C = [list(map(int, input().split())) for _ in range(3)]

A.sort()
C.sort()

ans = 0
for b in B:
	a = bisect_left(A, b)
	c = N-bisect_right(C, b)
	# print(b, (a, c))
	ans += a*c

print(ans)