from collections import deque
from itertools import chain

INF = 10**18

H, W = map(int, input().split())
A = [input() for _ in range(H)]

q = deque([])
dist = [[INF for _ in range(W)]for _ in range(H)]
for y, A_line in enumerate(A):
    for x, a in enumerate(A_line):
        if a == "#":
            dist[y][x] = 0
            q.append((x, y))

while q:
    t_pos = tx, ty = q.popleft()
    dist_t = dist[ty][tx]

    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        pos = x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        elif A[y][x] == "#":
            continue
        elif dist[y][x] <= dist_t + 1:
            continue
        dist[y][x] = dist_t + 1
        q.append(pos)
# print(dist)

r = max(chain(*dist))
print(r)