# https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b

from bisect import bisect_right

D = int(input())
N = int(input())
M = int(input())
D_list = [int(input()) for _ in range(N-1)]
K = [int(input()) for _ in range(M)]

D_list.sort()
stores = [0] + D_list + [D]
# print(stores)
ans = 0
for k in K:
	r = bisect_right(stores, k)
	l = r-1
	cost = min(abs(k-stores[l]), abs(k-stores[r]))
	ans += cost
print(ans)
