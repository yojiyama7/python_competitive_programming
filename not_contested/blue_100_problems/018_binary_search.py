# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja

# from bisect import bisect_left, bisect_right

def bisect_left(l, x):
	ok = 0
	ng = len(l)
	while abs(ok-ng) > 1:
		mid = (ok+ng)//2
		if l[mid] < x:
			ok = mid
		else:
			ng = mid
	return ok+1

def bisect_right(l, x):
	ok = 0
	ng = len(l)
	while abs(ok-ng) > 1:
		mid = (ok+ng)//2
		if l[mid] <= x:
			ok = mid
		else:
			ng = mid
	return ok+1

N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

S.sort()

ans = 0
for t in T:
	if bisect_right(S, t) - bisect_left(S, t):
		ans += 1
print(ans)
