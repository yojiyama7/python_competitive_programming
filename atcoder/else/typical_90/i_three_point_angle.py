# 三角関数苦手すぎ
# 二頂点から角度出すのですらむずいが？？？

# from icecream import ic
# print = ic

from math import atan, degrees
from bisect import bisect_left

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def to_deg(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	x, y = x2-x1, y2-y1
	if x == 0:
		return 90 if y > 0 else 270
	m = degrees(atan(y/x))
	if x < 0:
		m += 180
		m %= 360
	# print(XY[i], XY[j], m)
	return m

def to_180(a):
	if a <= 180:
		return a
	return 360 - a

max_num = 0
for i in range(N):
	angles = []
	for j in range(N):
		if i == j:
			continue
		a = to_deg(XY[i], XY[j])
		angles.append(a)
	angles.sort()
	# print(i, angles)
	for j in range(N-1):
		a = angles[j]
		x = bisect_left(angles, (a+180)%360)
		b1 = angles[x-1]
		b2 = angles[x%(N-1)]
		# print(a, b1, b2)
		# old_max_num = max_num
		max_num = max(
			to_180(abs(a-b1)),
			to_180(abs(a-b2)),
			max_num
		)
		# if old_max_num != max_num:
			# print(i, a, b1, b2)
print(max_num)
