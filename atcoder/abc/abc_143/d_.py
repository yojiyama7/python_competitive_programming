# 配列操作時間かかる
from bisect import bisect_left, bisect_right

N = int(input())
L = list(map(int, input().split()))

L.sort()

count = 0
for i, l1 in enumerate(L):
    for j, l2 in enumerate(L):
        if i < j:
            s = max(j+1, bisect_right(L, abs(l1-l2)))
            e = max(j+1, bisect_left(L, l1+l2))

            # print((i, j), (l1, l2), (abs(l1-l2), l1+l2), (s, e))
            count += max(0, e-s)
            # abs(l1-l2) <= m <= l1+l2

print(count)

# count = 0
# for i, l1 in enumerate(L):
#     for j, l2 in enumerate(L):
#         for k, l3 in enumerate(L):
#             if i < j < k:
#                 if a < b+c and b < c+a and c < a+b:
#                     count += 1
#                 print((i, j, k))

# i < j < k