# つながっている白マスは距離ゼロである

from collections import deque

INF = 10**18

H, W = map(int, input().split())
C = [input() for _ in range(H)]
# H, W = 500, 500
# C = [["."]*W for _ in range(H)]
# C[0][0] = "s"
# C[H-1][W-1] = "g"

for y, C_line in enumerate(C):
    for x, c in enumerate(C_line):
        if c == "s":
            s_pos = sx, sy = x, y
        elif c == "g":
            g_pos = gx, gy = x, y

dist = [[INF for _ in range(W)] for _ in range(H)]
dist[sy][sx] = 0
q = deque([s_pos])
while q:
    t_pos = tx, ty = q.popleft()
    t_dist = dist[ty][tx]

    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        pos = x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        if C[y][x] == "#":
            if dist[y][x] <= t_dist + 1:
                continue
            dist[y][x] = t_dist + 1
            q.append(pos)
        else:
            if dist[y][x] <= t_dist:
                continue
            dist[y][x] = t_dist
            q.appendleft(pos)

# [print(d[:4]) for d in dist[:4]]

# print(must_break)

if dist[gy][gx] <= 2:
    print("YES")
else:
    print("NO")