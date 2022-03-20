from math import sin, cos, radians

A, B, H, M = map(int, input().split())

at_d = (3-(H+M/60))%12 * 30
bt_d = (15-M)%60 * 6

# print(at_d, bt_d)

at_r = radians(at_d)
bt_r = radians(bt_d)

ax, ay = (cos(at_r)*A, sin(at_r)*A)
bx, by = (cos(bt_r)*B, sin(bt_r)*B)

r = ((ax-bx)**2 + (ay-by)**2)**(1/2)
print(r)