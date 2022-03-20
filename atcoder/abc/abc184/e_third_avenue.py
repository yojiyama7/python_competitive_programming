from collections import deque

INF = float("inf")

H, W = map(int, input().split())
A = [input() for _ in range(H)]
# H, W = 2000, 2000
# A = [["a" for _ in range(W)] for _ in range(H)]
# A[0][0] = 'S'
# # A[0][10] = 'a'
# # A[0][13] = 'a'
# A[H-1][W-1] = 'G'

is_used = [0]*26
tp_points = [list() for _ in range(26)]
sx, sy = -1, -1
gx, gy = -1, -1
for y, A_y in enumerate(A):
    for x, A_yx in enumerate(A_y):
        if A_yx == 'S':
            sx, sy = x, y
        elif A_yx == 'G':
            gx, gy = x, y
        elif ord('a') <= ord(A_yx) <= ord('z'):
            tp_points[ord(A_yx)-ord('a')].append((x, y))

dist = [[INF for _ in range(W)] for _ in range(H)]
dist[sy][sx] = 0
q = deque([(sx, sy)])
while q:
    t_pos = tx, ty = q.popleft()
    t_dist = dist[ty][tx]
    if tx == gx and ty == gy:
        break

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = tx+dx, ty+dy
        if not (0 <= x < W and 0 <= y < H):
            continue
        if A[y][x] == "#":
            continue
        if dist[y][x] <= t_dist + 1:
            continue
        dist[y][x] = t_dist + 1
        q.append((x, y))
    if ord('a') <= ord(A[ty][tx]) <= ord('z'):
        n = ord(A[ty][tx])-ord('a')
        if is_used[n]:
            continue
        is_used[n] = 1
        for pos in tp_points[n]:
            x, y = pos
            if dist[y][x] <= t_dist + 1:
                continue
            dist[y][x] = t_dist + 1
            q.append(pos)

# list(map(print, dist)) 
result = -1 if dist[gy][gx] == INF else dist[gy][gx]
print(result)
