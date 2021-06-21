from a_ import N
from math import gcd

L, R = map(int, input().split())

# print("-"*64)

# cnt = 0
# for x in range(L, R+1):
#     for y in range(L, R+1):
#         if gcd(x, y) not in [1, x, y]:
#             # print(x, y)
#             cnt += 1
#         else:
#             print(x, y)

# print("-"*64)

# print(cnt)

n = R-L+1

ans = 0
for x in range(L, R+1):
    a = n
    a -= R//x - (L-1)//x
    