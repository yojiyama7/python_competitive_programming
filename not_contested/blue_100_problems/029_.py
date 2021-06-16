# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

INF = float('inf')

R, C = map(int, input().split())
SY, SX = map(int, input().split())
GY, GX = map(int, input().split())
C_map = [input() for _ in range(R)]

sx, sy = SX-1, SY-1
gx, gy = GX-1, GY-1

dist = [[INF for _ in range(C)] for _ in range(R)]
dist[sy][sx] = 0

q = deque([(sx, sy)])
while q:
    tx, ty = q.popleft()

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = tx+dx, ty+dy
        if not (0 <= x < C and 0 <= y < R):
            continue
        if C_map[y][x] == '#':
            continue
        if dist[y][x] <= dist[ty][tx] + 1:
            continue
        dist[y][x] = dist[ty][tx] + 1
        q.append((x, y))

# list(map(print, dist))

print(dist[gy][gx])
