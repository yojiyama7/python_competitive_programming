# にぶたんgg
# bisect で帰ってきた値 は N に対して 0 <= x < N+1 なので
# 両端に気をつける
# 逆に両端について考えて x-1 と x が 候補だなと考える

from bisect import bisect_left

INF = float('inf')

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()
# print(A)
for b in B:
	x = bisect_left(A, b)
	ans = INF
	if x < N:
		ans = min(ans, A[x]-b)
	if x-1 >= 0:
		ans = min(ans, b-A[x-1])
	print(ans)
