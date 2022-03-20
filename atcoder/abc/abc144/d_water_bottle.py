from math import tan, radians, pi

A, B, X = map(int, input().split())

def solve(angle):
    c = A*tan(radians(angle))
    if c <= B:
        max_water = A*B - (A*c/2)
    else:
        d = B*tan(radians(90-angle))
        max_water = B*d/2
    return max_water >= X/A

ok = 0
ng = 90
for i in range(30):
    mid = (ok+ng)/2
    # print(mid, angle_to_max_water(mid))
    if solve(mid):
        ok = mid
    else:
        ng = mid
    # print(l, r)

print(ok)