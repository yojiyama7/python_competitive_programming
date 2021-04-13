H, W, A, B = map(int, input().split())

tile = [[0 for _ in range(W)] for _ in range(H)]

def solve(i, placed):
    # print(i, placed, tile)
    if i == H*W:
        return (placed == A)
    elif placed == A:
        return (1)
    x, y = i%W, i//W
    cnt = 0
    if 0 <= x < W and 0 <= x+1 < W:
        if tile[y][x] == 0 and tile[y][x+1] == 0:
            tile[y][x] = 1
            tile[y][x+1] = 1
            cnt += solve(i+1, placed+1)
            tile[y][x] = 0
            tile[y][x+1] = 0
    if 0 <= y < H and 0 <= y+1 < H:
        if tile[y][x] == 0 and tile[y+1][x] == 0:
            tile[y][x] = 1
            tile[y+1][x] = 1
            cnt += solve(i+1, placed+1)
            tile[y][x] = 0
            tile[y+1][x] = 0
    cnt += solve(i+1, placed)
    return (cnt)

print(solve(0, 0))