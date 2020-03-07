N = int(input())
C = list(map(int, input().split()))
Q = int(input())
S = [list(map(int, input().split())) for _ in range(Q)]

################################

# N = int(input())
# C = list(map(int, input().split()))
# Q = int(input())
# S = [list(map(int, input().split())) for _ in range(Q)]

# even_min = min(C[1::2])
# odd_min = min(C[::2])
# even_count = 0
# odd_count = 0

# sum_num = 0
# for s in S:
#     if s[0] == 1:
#         x, a = s[1:]
#         x -= 1
#         c = C[x] - [odd_count, even_count][x%2]
#         if c - a >= 0:
#             C[x] -= a
#             sum_num += a
#     elif s[0] == 2:
#         a = s[1]
#         c = odd_min - odd_count
#         if c - a >= 0:
#             odd_min -= a
#             odd_count += a
#             sum_num += a*-(-N//2)
#     else:
#         a = s[1]
#         c = min(odd_min-odd_count, even_min-even_count)
#         if c - a >= 0:
#             odd_min -= a
#             even_min -= a
#             odd_count += a
#             even_count += a
#             print("a", sum_num, a*N)
#             sum_num += a*N
#     print(sum_num)

# print(sum_num)