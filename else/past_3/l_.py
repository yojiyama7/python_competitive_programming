from collections import deque

N = int(input())
KT = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
A = list(map(int, input().split()))

K, T = [], []
for i, (k, *t) in enumerate(KT):
    K.append(k)
    T.append([(-t_j, t_j, (i, j)) for j, t_j in enumerate(t)])



################################

# from heapq import *

# N = int(input())
# KT = [list(map(int, input().split())) for _ in range(N)]
# M = int(input())
# A = list(map(int, input().split()))

# K, T = [], []
# for i, (k, *t) in enumerate(KT):
#     K.append(k)
#     T.append([(-t_j, t_j, (i, j)) for j, t_j in enumerate(t)])

# first, second = [], []
# for i, t in enumerate(T):
#     first.append(t[0])
#     second.append(t[1])

# heapify(first)
# heapify(second)

# invalid_second = [[0]*k for k in K]

# for i, a in enumerate(A):
#     if a == 1:
#         _, x, (x_id, x_id2) = heappop(first)
#         print(x)
#         invalid_second[x_id][x_id2+1] = 1
#         heappush(first, T[x_id][x_id2+1])
#     elif a == 2:
#         # x > y
#         x_, y_ = sorted([heappop(first), heappop(second)])
#         (_, x, (x_id, x_id2)), (_, y, (y_id, y_id2)) = x_, y_
#         if invalid_second[x_id][x_id2]:
#             print(y)
#         else:
#             print(x)
#             heappush(first, y_)
#     print(first, second)


    