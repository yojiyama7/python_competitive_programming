# H, W, T = map(int, input().split(" "))
# S = [input() for _ in range(H)]

# BIG_NUM = 10**18

# for i, l in enumerate(S):
#     if "S" in l:
#         start_pos = start_x, start_y = (l.find("S"), i)
#         break

# ADS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# def dfs(x):
#     m = [[BIG_NUM for _ in range(W)] for _ in range(H)]
#     m[start_y][start_x] = 0
#     q = [start_pos]
#     while q:
#         this_pos = this_x, this_y = q.pop()
#         if S[this_y][this_x] == "G":
#             return 

#         for ad_x, ad_y in ADS:
#             pos = x, y = this_x+ad_x, this_y+ad_y
#             if not (0 <= x < W and 0 <= y < H):
#                 continue
#             if m[y][x] == BIG_NUM:
#                 continue
#             m[y][x] = min(
#                 m[y][x],
#                 m[this_y][this_x] + (x if S[y][x] == "#" else 1)
#             )
#             q.append(pos)

################################

# H, W, T = map(int, input().split(" "))
# S = [input() for _ in range(H)]

# def min_route(m, x):

################################

# 二分探索、、、　浮かばんかったなぁ、、、
# 特定の値xを求めたいときに x=i のときYesなら x<i もYes、
# x=i のときNoなら x>i もNo
# (あるNoより左はNo、あるYesより右はYes)
# というときは、二分探索が使える

################################
# わからんのだよなぁ　どこ基準でなのか

# from collections import deque

# ADS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# H, W, T = map(int, input().split(" "))
# S = [list(input()) for _ in range(H)]

# for y, line in enumerate(S):
#     if "S" in line:
#         s_pos = s_x, s_y = (line.index("S"), y)
#     if "G" in line:
#         g_pos = g_x, g_y = (line.index("G"), y)

# costs = [[10**9 for _ in range(W)] for _ in range(H)]
# costs[s_y][s_x] = 0

# q = deque([s_pos])
# while q:
#     this_pos = this_x, this_y = q.popleft()
#     # if this_pos == g_pos:
#     #     break
#     this_num = costs[this_y][this_x]

#     for ad_x, ad_y in ADS:
#         pos = x, y = this_x+ad_x, this_y+ad_y
#         if not(0 <= x < W and 0 <= y < H):
#             continue

#         is_black = (S[y][x] == "#")
#         cost = this_num + (100 if is_black else 1)
#         if cost <= costs[y][x]:
#             costs[y][x] = cost
#             if is_black:
#                 q.append(pos)
#             else:
#                 q.appendleft(pos)

# g_cost = costs[g_y][g_x]
# white, black = g_cost%100, g_cost//100
# print(white, black)
# print((T-white)//black)