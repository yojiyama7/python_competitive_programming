H, W = map(int, input().split())
S = [input() for _ in range(H)]



################################

# 辺数えるほうが何言ってるかわかりやすいな
# 頂点基準の解放も何を言っているかぐらいはわかりたい

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
