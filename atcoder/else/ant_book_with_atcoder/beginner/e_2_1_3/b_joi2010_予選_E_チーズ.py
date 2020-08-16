# JOI 2010 予選 E チーズ
# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

from collections import deque

INF = 10**18

H, W, N = map(int, input().split())
S = [input() for _ in range(H)]
# H, W, N = 1000, 1000, 9
# S = [["."]*W for _ in range(H)]
# S[0][0] = "S"
# for i in range(1, N+1):
#     S[(i*30943+293)%H][(i*4329+432)%W] = str(i)
# print(len(S))

sg_pos_list = [None]*(N+1)
for y, S_line in enumerate(S):
    for x, c in enumerate(S_line):
        if c == "." or c == "X":
            pass
        elif c == "S":
            sg_pos_list[0] = (x, y)
        else:
            int_c = int(c)
            sg_pos_list[int_c] = (x, y) 

# print("s")
sum_num = 0
for i in range(N):
    # print(i)
    s_pos = sx, sy = sg_pos_list[i]
    g_pos = gx, gy = sg_pos_list[i+1]
    dist = [[INF for _ in range(W)] for _ in range(H)]
    dist[sy][sx] = 0
    q = deque([s_pos])
    # _c = 0
    while q:
        t_pos = tx, ty = q.popleft()
        t_dist = dist[ty][tx]

        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            # _c += 1
            pos = x, y = tx+dx, ty+dy
            if not (0 <= x < W and 0 <= y < H):
                continue
            elif S[y][x] == "X":
                continue
            elif dist[y][x] <= (t_dist + 1):
                continue
            dist[y][x] = t_dist + 1
            q.append(pos)  
    # print(_c)
    # print(gx, gy)
    sum_num += dist[gy][gx]

print(sum_num)

################################

# # AC

# from collections import deque
# import sys
# sys.setrecursionlimit(10**8)

# Ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# H, W, N = map(int, input().split())
# C = [list(input()) for _ in range(H)]
# # H, W, N = 1000, 1000, 1
# # C = [["."]*1000 for _ in range(1000)]
# # C[0][0] = "S"
# # C[999][999] = "1"

# points = [(-1, -1)]*(N+1)
# for i, C_line in enumerate(C):
#     for j in range(N+1):
#         t = str(j) if j else "S"
#         if t in C_line:
#             # print(C_line, i, j, t)
#             points[j] = (C_line.index(t), i)

# # print(points)

# def bfs(s_pos, g_pos):
#     sx, sy = s_pos
#     route = [[10**18]*W for _ in range(H)]
#     route[sy][sx] = 0
#     q = deque([s_pos])
#     while q:
#         t_pos = tx, ty = q.popleft()
#         tr = route[ty][tx]
#         if t_pos == g_pos:
#             return tr

#         for dx, dy in Ds:
#             pos = x, y = tx+dx, ty+dy
#             if not (0 <= x < W and 0 <= y < H) or C[y][x] == "X" or route[y][x] != (10**18):
#                 continue
#             route[y][x] = tr+1
#             q.append(pos)
#         # [print(r[:6]) for r in route[:6]]
 
# sum_num = 0
# for i in range(N):
#     sum_num += bfs(points[i], points[i+1])

# print(sum_num)