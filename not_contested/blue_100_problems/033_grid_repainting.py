# https://atcoder.jp/contests/abc088/tasks/abc088_d

from collections import deque

INF = float('inf')

H, W = map(int, input().split())
S = [input() for _ in range(H)]

white = sum(s.count('.') for s in S)

dist = [[INF for _ in range(W)] for _ in range(H)]
dist[0][0] = 1

q = deque([(0, 0)])
while q:
    tx, ty = q.popleft()
    # print(tx, ty)

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        if S[y][x] == '#':
            continue
        if dist[y][x] <= dist[ty][tx] + 1:
            continue
        dist[y][x] = dist[ty][tx] + 1
        q.append((x, y))

# list(map(print, dist))
if dist[H-1][W-1] == INF:
    print(-1)
else:
    print(white - dist[H-1][W-1])
