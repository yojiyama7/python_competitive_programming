from math import atan, degrees

N = int(input())
X0, Y0 = map(int, input().split())
Xh, Yh = map(int, input().split())

cx, cy = (X0+Xh)/2, (Y0+Yh)/2
angle = degrees(atan((Y0-cy)/(X0-cx)))
print(angle)