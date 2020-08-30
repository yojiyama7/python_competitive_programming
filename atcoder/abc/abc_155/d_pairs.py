# 正負の数の積に関するものは、積が負, 0, 正になるパターンで場合分けする

# K番目(二分探索感)

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

K

# l = []
# m = []
# for i, a in enumerate(A):
#     for j, b in enumerate(A):
#         if i < j:
#             l.append(a*b)
#             m.append((a, b))

# l.sort()

# print(l[K-1])

# [print(x) for x in sorted(m, key=lambda x: x[0]*x[1])]