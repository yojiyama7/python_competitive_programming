# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

import sys
sys.setrecursionlimit(10**8)

from itertools import product

ans_list = []

while True:
    W, H = map(int, input().split())
    if W == H == 0:
        break
    C = [list(map(int, input().split())) for _ in range(H)]

    visited = [[0 for _ in range(W)] for _ in range(H)]
    def dfs(cx, cy):
        if not (0 <= cx < W and 0 <= cy < H):
            return 0
        if visited[cy][cx]:
            return 0
        if C[cy][cx] == 0:
            return 0
        visited[cy][cx] = 1
        for dy, dx in product(range(-1, 2), repeat=2):
            x, y = cx+dx, cy+dy
            dfs(x, y)
        return 1
    ans = 0
    for y in range(H):
        for x in range(W):
            ans += dfs(x, y)
    ans_list.append(ans)

for ans in ans_list:
    print(ans)
