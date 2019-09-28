# AOJ 1160 島はいくつある？
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

import sys
sys.setrecursionlimit(10**8)

def dfs_fill(m, x, y):
    if not (0 <= x < W and 0 <= y < H) or m[y][x] == "0":
        return False
    m[y][x] = "0"
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            dfs_fill(m, x+dx, y+dy)

while True:
    W, H = map(int, input().split())
    if W == H == 0:
        break
    C = [input().split() for _ in range(H)]

    count = 0
    for y in range(H):
        for x in range(W):
            # print("\n".join(["".join(c) for c in C]))
            if C[y][x] == "1":
                count += 1
                dfs_fill(C, x, y)

    print(count)