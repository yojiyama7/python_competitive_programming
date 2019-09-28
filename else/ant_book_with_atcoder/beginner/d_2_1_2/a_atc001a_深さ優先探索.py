# ATC 001 A 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a

################################

# 破壊的でも return 使わない再帰の方が強い

import sys
sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

def dfs(x, y):
    if not (0 <= x < W and 0 <= y < H) or C[y][x] == "#":
        return False
    C[y][x] = "#"
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

s_x, s_y = (-1, -1)
g_x, g_y = (-1, -1)
for y, C_line in enumerate(C):
    if "s" in C_line:
        s_x, s_y = (C_line.index("s"), y)
    if "g" in C_line:
        g_x, g_y = (C_line.index("g"), y)

dfs(s_x, s_y)

print("Yes" if C[g_y][g_x] == "#" else "No")

################################

# # 再帰はメモリ実行時間ともに重い

# import sys
# sys.setrecursionlimit(10**8)

# Ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# H, W = map(int, input().split())
# C = [list(input()) for _ in range(H)]

# def dfs(tx, ty):
#     if not (0 <= tx < W and 0 <= ty < H) or C[ty][tx] == "#":
#         return False
#     if C[ty][tx] == "g":
#         return True
#     C[ty][tx] = "#"
#     for dx, dy in Ds:
#         x, y = tx+dx, ty+dy
#         if dfs(x, y):
#             return True
#     return False

# s_x, s_y = (-1, -1)
# for y, C_line in enumerate(C):
#     if "s" in C_line:
#         s_x, s_y = (C_line.index("s"), y)

# print("Yes" if dfs(s_x, s_y) else "No")
