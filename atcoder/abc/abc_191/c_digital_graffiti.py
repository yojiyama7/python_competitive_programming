# 辺を数える

from itertools import groupby

H, W = map(int, input().split())
S = [input() for _ in range(H)]

cnt = 0
for y in range(H-1):
    cnt += len(list(groupby(S[y][x] == S[y+1][x] for x in range(W-1)))) // 2
for x in range(W-1):
    cnt += len(list(groupby(S[y][x] == S[y][x+1] for y in range(H-1)))) // 2

print(cnt)

################################

# 辺数えるほうが何言ってるかわかりやすいな
# 頂点基準の解法も何を言っているかぐらいはわかりたい

# # WA

# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# sum_num = 0
# for cy in range(1, H-1):
#     for cx in range(1, W-1):
#         if S[cy][cx] == ".":
#             continue
#         cnt = 0
#         for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#             x, y = cx+dx, cy+dy
#             cnt += (S[y][x] == "#")
#         if cnt in [1, 3]:
#             sum_num += 1

# print(sum_num)
