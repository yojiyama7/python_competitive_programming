# from functools import lru_cache
# from collections import deque
# import sys

# input = sys.stdin.readline

# H, W = map(int, input().split(" "))
# C = [input() for _ in range(H)]


# # memo = dict()


# @lru_cache(maxsize=None)
# def count_num(n, k):
#     # if (n, k) in memo:
#     #     return memo[(n, k)]
#     c = 0
#     while n % k == 0:
#         # print((n, k))
#         n //= k
#         c += 1
#     # memo[(n, k)] = c
#     return c

# counts = [0, 0, 0]

# visited = [[False]*W for _ in range(H)]
# for i, c_line in enumerate(C):
#     for j, c in enumerate(c_line[:W]):
#         if c == ".":
#             continue
#         if visited[i][j]:
#             continue
#         visited[i][j] = True

#         black_count = 1
#         q = deque([(j, i)])
#         while q:
#             this_pos = this_x, this_y = q.pop()

#             for ad_y in range(-1, 2):
#                 for ad_x in range(-1, 2):
#                     if ad_x == ad_y == 0:
#                         continue
                        
#                     pos = x, y = this_x+ad_x, this_y+ad_y
#                     if not (0 <= x < W and 0 <= y < H):
#                         continue
#                     if C[y][x] == ".":
#                         continue
#                     if visited[y][x]:
#                         continue
#                     visited[y][x] = True
#                     black_count += 1
#                     q.append(pos)

#         if count_num(black_count, 11) % 2 == 1:
#             t = 2
#         elif count_num(black_count, 3) % 2 == 1:
#             t = 0
#         else:
#             t = 1
#         # print(black_count, t, (count_num(black_count, 11), count_num(black_count, 3)))

#         counts[t] += 1

# print(*counts)
