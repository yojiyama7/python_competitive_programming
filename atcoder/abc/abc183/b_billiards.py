SX, SY, GX, GY = map(int, input().split())

ax, ay = SX, -SY
bx, by = GX, GY

dx, dy = bx-ax, by-ay

print(ax + abs(ay)/dy * dx)