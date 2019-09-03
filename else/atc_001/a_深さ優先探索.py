import sys
sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

# 各行において、sが入っているか調べ、入っていたら、インデックスを記録
for i, c_line in enumerate(C):
    if "s" in c_line:
        s_x, s_y = c_line.index("s"), i

# posからゴールにたどり着けるか
def dfs(x, y):
    # x, y = pos
    if not (0 <= x < W and 0 <= y < H):
        return False
    if C[y][x] == "#":
        return False
    if C[y][x] == "g":
        print("Yes")
        exit()
    C[y][x] = "#"

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(s_x, s_y)
print("No")