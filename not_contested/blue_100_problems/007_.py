# https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c

# import sys
# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", 'w')

from itertools import combinations as combi

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY_set = set(map(tuple, XY))

max_num = 0
# combinations を使って 定数倍効率をあげる
for (a, b), (c, d) in combi(XY, 2):
		x, y = c-a, d-b
		e, f = c+y, d-x
		g, h = a+y, b-x
		if (e, f) in XY_set and (g, h) in XY_set:
			score = 2*x*y + abs(x-y)**2
			max_num = max(score, max_num)

print(max_num)
