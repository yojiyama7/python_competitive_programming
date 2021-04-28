N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

# 分割後全てが x[cm] 以上になるように羊羹を切ったとき
# K+1[個] 以上に分割できるか
def is_ok(x):
	b = 0
	cnt = 0
	for a in A:
		if (a - b) >= x:
			cnt += 1
			b = a
	if (L - b) >= x:
		cnt += 1
	return (cnt >= K+1)

ok, ng = 0, L
while abs(ok-ng) > 1:
	mid = (ok+ng)//2
	if is_ok(mid):
		ok = mid
	else:
		ng = mid

print(ok)
