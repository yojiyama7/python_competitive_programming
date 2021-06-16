# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e

from collections import deque

DPOS_left = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, 0),
]

DPOS_right = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

DPOS = [DPOS_left, DPOS_right]

W, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

w, h = W+2, H+2
A_wrapped = [[0]*w] + [[0]+a+[0] for a in A] + [[0]*w]

ans = 0
visited = [[0 for _ in range(w)] for _ in range(h)]
visited[0][0] = 1
q = deque([(0, 0)])
while q:
    tx, ty = q.popleft()

    for dx, dy in DPOS[ty%2]:
        x, y = tx+dx, ty+dy
        if not (0 <= x < w and 0 <= y < h):
            continue
        if visited[y][x]:
            continue
        if A_wrapped[y][x] == 1:
            ans += 1
            continue
        visited[y][x] = 1
        q.append((x, y))

    # for i, line in enumerate(visited):
    #     s = ""
    #     if i%2:
    #         s = " "
    #     s += ' '.join(map(str, line))
    #     print(s)
    # print()

print(ans)