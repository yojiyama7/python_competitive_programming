from collections import deque

INF = 10**18

H, W = map(int, input().split())
S = [input() for _ in range(H)]

live_cell_count = 0
for S_line in S:
    live_cell_count += S_line.count(".")

dist = [[INF for _ in range(W)] for _ in range(H)]
dist[0][0] = 0
q = deque([(0, 0)])
while q:
    t_pos = tx, ty = q.popleft()
    t_dist = dist[ty][tx]

    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        pos = x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        elif S[y][x] == "#":
            continue
        elif dist[y][x] <= t_dist + 1:
            continue
        dist[y][x] = t_dist + 1
        q.append(pos)
# print(dist)

if dist[H-1][W-1] == INF:
    print(-1)
else:
    print(live_cell_count - dist[H-1][W-1] - 1)