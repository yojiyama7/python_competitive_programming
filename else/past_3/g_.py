from collections import deque
import sys
sys.setrecursionlimit(10**8)

N, X, Y = map(int, input().split())
OXY = [list(map(int, input().split())) for _ in range(N)]

D_POS = [(1, 1), (0, 1), (-1, 1), (1, 0), (-1, 0), (0, -1)]

grid = [["." for _ in range(410)] for _ in range(410)]
grid[205+Y][205+X] = "G"
for ox, oy in OXY:
    ox, oy = ox+205, oy+205
    grid[oy][ox] = "#"
grid[205][205] = "#"

min_routes = [[10**18 for _ in range(410)] for _ in range(410)]
min_routes[205][205] = 0

q = deque([(205, 205)])
while q:
    # print(q)
    tx, ty = q.popleft()
    t_mr = min_routes[ty][tx]
    # print(tx, ty, t_mr)
    if grid[ty][tx] == "G":
        break

    for dx, dy in D_POS:
        x, y = tx+dx, ty+dy
        if not (0 <= x < 410 and 0 <= y < 410):
            continue
        if grid[y][x] == "#":
            continue
        if min_routes[y][x] <= t_mr + 1:
            continue
        grid[y][x] = "#"
        min_routes[y][x] = t_mr + 1
        q.append((x, y))

print(-1 if min_routes[205+Y][205+X] >= 10**18 else min_routes[205+Y][205+X])
