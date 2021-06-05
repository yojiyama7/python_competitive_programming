# https://atcoder.jp/contests/abc145/tasks/abc145_c

from itertools import permutations as permu

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

sum_num = 0
cnt = 0
for l in permu(XY):
	bx, by = l[0]
	for x, y in l[1:]:
		sum_num += ((x-bx)**2 + (y-by)**2) ** (1/2)
		bx, by = x, y
	cnt += 1

print(sum_num / cnt)
