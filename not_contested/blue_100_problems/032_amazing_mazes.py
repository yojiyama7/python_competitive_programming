# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp

from itertools import product
from collections import deque

INF = float('inf')

ans_list = []

while True:
    W, H = map(int, input().split())
    if W == H == 0:
        break
    A = [list(map(int, input().split())) for _ in range(2*H-1)]

    # g = dict()
    # for y, x in product(range(H), range(W)):
    #     g[(x, y)]
    #     # left
    #     (x-1, 2*y)
    #     (x, 2*y)
    #     (x, 2*y-1)


    h, w = 2*H-1, 2*W-1
    maze = [[int(j%2 == i%2 == 1) for j in range(w)] for i in range(h)]
    # list(map(print, maze))

    for i, a in enumerate(A):
        for j, c in enumerate(a):
            y, x = i, 2*j + (i%2 == 0)
            # print(x, y)
            maze[y][x] = c
    # list(map(print, maze))

    dist = [[INF for _ in range(w)] for _ in range(h)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    while q:
        tx, ty = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = tx+dx, ty+dy
            if not (0 <= x < w and 0 <= y < h):
                continue
            if maze[y][x]:
                continue
            if dist[y][x] <= dist[ty][tx] + 1:
                continue
            dist[y][x] = dist[ty][tx] + 1
            q.append((x, y))

    # list(map(print, maze))
    # list(map(print, dist))
    # print()
    ans = 0 if dist[h-1][w-1] == INF else dist[h-1][w-1]//2+1
    ans_list.append(ans)

list(map(print, ans_list))
