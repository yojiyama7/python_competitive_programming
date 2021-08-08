from collections import deque

INF = 10**20

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dpos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
break_dpos = []
for y in range(-2, 3):
    for x in range(-2, 3):
        if abs(y)+abs(x) == 4 or y == x == 0:
            continue
        break_dpos.append((x, y))

dist = [[INF for _ in range(W)] for _ in range(H)]
dist[0][0] = 0
q = deque([(0, 0)])
while q:
    tx, ty = q.popleft()
    for dx, dy in dpos:
        x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        if S[y][x] == '#':
            continue
        if dist[y][x] <= dist[ty][tx]:
            continue
        dist[y][x] = dist[ty][tx]
        q.appendleft((x, y))
    for dx, dy in break_dpos:
        x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        if dist[y][x] <= dist[ty][tx] + 1:
            continue
        dist[y][x] = dist[ty][tx] + 1
        q.append((x, y))

print(dist[H-1][W-1])

################################

# from collections import deque

# INF = 10**20

# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# black_dpos = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
# white_dpos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# dist = [[INF for _ in range(W)] for _ in range(H)]
# dist[0][0] = 0
# q = deque([(0, 0)])
# while q:
#     tx, ty = q.popleft()
#     for dx, dy in white_dpos:
#         x, y = tx+dx, ty+dy
#         if not (0 <= x < W and 0 <= y < H):
#             continue
#         status = S[ty][tx]+S[y][x]
#         if status == '..':
#             cost = 0
#         elif status == '.#':
#             cost = 2
#         elif status == '#.':
#             cost = dist[ty][tx]%2
#         else:
#             cost = 1
#         if dist[y][x] <= dist[ty][tx] + cost:
#             continue
#         dist[y][x] = dist[ty][tx] + cost
#         if cost:
#             q.append((x, y))
#         else:
#             q.appendleft((x, y))
#     # for dx, dy in black_dpos:
#     #     x, y = tx+dx, ty+dy
#     #     if not (0 <= x < W and 0 <= y < H):
#     #         continue
#     #     status = S[ty][tx]+S[y][x]
#     #     cost = INF
#     #     if status == '##':
#     #         cost = 1
#     #     if dist[y][x] <= dist[ty][tx] + cost:
#     #         continue
#     #     dist[y][x] = dist[ty][tx] + cost
#     #     if cost:
#     #         q.append((x, y))
#     #     else:
#     #         q.appendleft((x, y))

# print(*dist, sep='\n')

# print(dist[H-1][W-1]//2)