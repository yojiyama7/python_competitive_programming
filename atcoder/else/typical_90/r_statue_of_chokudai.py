from math import sin, cos, radians, acos, degrees

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

for e in E:
	deg = 360 - (e/T*360+90)%360
	rad = radians(deg)
	y1 = 0 + cos(rad)*(L/2)
	z1 = (L/2) + sin(rad)*(L/2)
	x, y, z = abs(X-0), abs(Y-y1), abs(0-z1)
	c = (x**2 + y**2)**(1/2)
	d = (c**2 + z**2)**(1/2)
	theta = acos(c/d)
	theta_deg = degrees(theta)
	print(theta_deg)
