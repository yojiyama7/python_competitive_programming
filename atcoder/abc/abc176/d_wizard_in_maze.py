from collections import deque
from itertools import product

INF = 10**18

H, W = map(int, input().split())
C = list(map(int, input().split()))
D = list(map(int, input().split()))
S = [input() for _ in range(H)]

# H, W = 10**3, 10**3
# C = [1, 1]
# D = [H, W]
# S = [["."]*W]*H
# S[24] = ["#"]*W
# for y in range(H):
#     S[y][234] = "#"
#     S[y][236] = "#"
# print("p")

# H, W = 5, 5
# C = [1, 1]
# D = [3, 3]
# S = [
#     ".....",
#     "####.",
#     "...#.",
#     ".###.",
#     ".....",
# ]

s_pos = sx, sy = C[1]-1, C[0]-1
g_pos = gx, gy = D[1]-1, D[0]-1

# dist init
dist = [[INF for _ in range(W)] for _ in range(H)]
dist[sy][sx] = 0
# visited init
visited = [[0 for _ in range(W)] for _ in range(H)]
q = deque([s_pos])

while q:
    t_pos = tx, ty = q.popleft()
    t_dist = dist[ty][tx]

    if visited[ty][tx]:
        continue
    # visited edit
    visited[ty][tx] = 1

    for dx, dy in product(range(-2, 3), repeat=2):
        if dx == dy == 0:
            continue
        pos = x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        if S[y][x] == "#":
            continue
        cost = int(abs(dx)+abs(dy) > 1)
        if dist[y][x] <= t_dist + cost:
            continue
        # dist edit
        dist[y][x] = t_dist + cost
        if cost == 0:
            q.appendleft(pos)
        else:
            q.append(pos)

r = dist[gy][gx]
if r == INF:
    print(-1)
else:
    print(r)