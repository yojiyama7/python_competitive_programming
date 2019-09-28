# ABC 007 C 幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

Ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

H, W = map(int, input().split())
SY, SX = map(int, input().split())
GY, GX = map(int, input().split())
C = [list(input()) for _ in range(H)]

def bfs(s_pos, g_pos):
    s_x, s_y = s_pos
    min_route = [[10**18]*W for _ in range(H)]
    min_route[s_y][s_x] = 0
    q = deque([s_pos])
    while q:
        t_pos = tx, ty = q.popleft()
        tr = min_route[ty][tx]
        for dx, dy in Ds:
            x, y = tx+dx, ty+dy
            if not (0 <= x < W and 0 <= y < H) or C[y][x] == "#":
                continue
            min_route[y][x] = min(min_route[y][x], tr+1)
            C[y][x] = "#"
            q.append((x, y))
    g_x, g_y = g_pos
    # [print(["x" if r_i == 10**18 else r_i for r_i in r]) for r in min_route]
    return min_route[g_y][g_x]

print(bfs((SX-1, SY-1), (GX-1, GY-1)))