# 一回もバグらせないことありますか？

from collections import deque
from itertools import chain

INF = 10**18

H, W = map(int, input().split())
S = [input() for _ in range(H)]

def check_max_route(sx, sy):
    r = [[INF for _ in range(W)] for _ in range(H)]
    r[sy][sx] = 0
    q = deque([(sx, sy)])
    while q:
        tx, ty = q.popleft()
        tr = r[ty][tx]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = tx+dx, ty+dy
            if not (0 <= x < W and 0 <= y < H):
                continue
            if S[y][x] == "#":
                continue
            if r[y][x] <= tr+1:
                continue
            r[y][x] = tr+1
            q.append((x, y))
    
    m = max([x for x in chain(*r) if x != INF])
    return m

max_num = 0
for sy in range(H):
    for sx in range(W):
        if S[sy][sx] == "#":
            continue
        m = check_max_route(sx, sy)
        max_num = max(max_num, m)

print(max_num)