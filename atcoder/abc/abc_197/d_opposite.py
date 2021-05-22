# 角度をわざわざ degrees にしなくてもいいんじゃね？
# 数学の角度は 真右が0度の反時計回り
# atan と atan2 の違いを考えて なんで atan2 の方がうまくいくのか
# from icecream import ic
# print = ic

from math import atan2, sin, cos, tan, pi, degrees

N = int(input())
X0, Y0 = map(int, input().split())
Xh, Yh = map(int, input().split())

cx, cy = (X0+Xh)/2, (Y0+Yh)/2
# print(cx, cy)
w, h = (X0-cx), (Y0-cy)
rad = atan2(h, w)
# print(rad, degrees(rad))
rad += 2*pi/N
# print(rad, degrees(rad))
r = (w**2 + h**2) ** (1/2)
dx, dy = cos(rad)*r, sin(rad)*r
# print(dx, dy)
x1, y1 = cx+dx, cy+dy
print(x1, y1)

################################

# from math import atan, degrees

# N = int(input())
# X0, Y0 = map(int, input().split())
# Xh, Yh = map(int, input().split())

# cx, cy = (X0+Xh)/2, (Y0+Yh)/2
# angle = degrees(atan((Y0-cy)/(X0-cx)))
# print(angle)