# ARC 004 A 2点間距離の最大値
# https://atcoder.jp/contests/arc004/tasks/arc004_1

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

max_size = 0
for x1, y1 in XY:
    for x2, y2 in XY:
        size = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
        max_size = max(max_size, size)

print(max_size)