# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

from collections import deque
from itertools import product

INF = float('inf')

H, W, N = map(int, input().split())
A = [input() for _ in range(H)]

cheeses = [None]*(N+1)
for y, x in product(range(H), range(W)):
    if A[y][x] in "X.":
        continue
    if A[y][x] == 'S':
        cheeses[0] = (x, y)
    else:
        cheeses[int(A[y][x])] = (x, y)

ans = 0
for i in range(N):
    sx, sy = cheeses[i]
    gx, gy = cheeses[i+1]
    dist = [[INF for _ in range(W)] for _ in range(H)]
    dist[sy][sx] = 0
    q = deque([(sx, sy)])
    while q:
        tx, ty = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = tx+dx, ty+dy
            if not (0 <= x < W and 0 <= y < H):
                continue
            if A[y][x] == 'X':
                continue
            if dist[y][x] <= dist[ty][tx] + 1:
                continue
            dist[y][x] = dist[ty][tx] + 1
            q.append((x, y))
    # print(dist)
    ans += dist[gy][gx]

print(ans)
