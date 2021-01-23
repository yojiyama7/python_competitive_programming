from itertools import chain

H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
# H, W, N, M = 1500, 1500, 5 * 10**5, 10**5
# AB = [(i%W, i//W) for i in range(N)]
# CD = [(i%W, i//W) for i in range(N, N+M)]

map_data = [[0 for _ in range(W)] for _ in range(H)]
for a, b in AB:
    a, b = a-1, b-1
    map_data[a][b] = 2
for c, d in CD:
    c, d = c-1, d-1
    map_data[c][d] = -1
map_data_2 = [l[:] for l in map_data[:]]

for y in range(H):
    for x in range(W-1):
        if map_data[y][x+1] == 0 and map_data[y][x] > 0:
            map_data[y][x+1] = 1
for y in range(H):
    for x in reversed(range(W-1)):
        if map_data[y][x] == 0 and map_data[y][x+1] > 0:
            map_data[y][x] = 1

for y in range(H-1):
    for x in range(W):
        if map_data_2[y+1][x] == 0 and map_data_2[y][x] > 0:
            map_data_2[y+1][x] = 1
for y in reversed(range(H-1)):
    for x in range(W):
        if map_data_2[y][x] == 0 and map_data_2[y+1][x] > 0:
            map_data_2[y][x] = 1

# [print(l) for l in map_data]

score = 0
for y in range(H):
    for x in range(W):
        if map_data[y][x] > 0 or map_data_2[y][x] > 0:
            score += 1
print(score)