# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d

M = int(input())
A = [tuple(map(int, input().split())) for _ in range(M)]
N = int(input())
B = [tuple(map(int, input().split())) for _ in range(N)]

sx, sy = A[0]
stars = [(x-sx, y-sy) for (x, y) in A]

B_set = set(B)

for cx, cy in B:
	if all((cx+dx, cy+dy) in B_set for dx, dy in stars):
		print(cx-sx, cy-sy)
		break
