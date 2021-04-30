from itertools import accumulate as acc

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

a = [0]*N
b = [0]*N
for i, (c, p) in enumerate(CP):
	if c == 1:
		a[i] = p
	else:
		b[i] = p

a_acc = [0] + list(acc(a))
b_acc = [0] + list(acc(b))

for l, r in LR:
	l, r = l-1, r
	x = a_acc[r] - a_acc[l]
	y = b_acc[r] - b_acc[l]
	print(x, y)
