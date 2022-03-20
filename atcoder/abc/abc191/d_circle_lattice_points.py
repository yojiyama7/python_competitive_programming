# 誤差はDecimal 以上

from decimal import Decimal
from math import ceil, floor

X, Y, R = map(Decimal, input().split())

cnt = 0 
for x in range(ceil(X-R), floor(X+R)+1):
    w = abs(x - X)
    h = (R**2 - w**2).sqrt()
    cnt += floor(Y+h) - ceil(Y-h) + 1

print(cnt)

################################

# # はい誤差
# Decimal でしたGG

# # WA

# from fractions import Fraction
# from math import ceil, floor

# def square_root(a):
#     ok, ng = 0, a
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if mid ** 2 <= a:
#             ok = mid
#         else:
#             ng = mid
#     return (ok)

# X, Y, R = map(Fraction, input().split())

# # print(X, Y, R, ceil(X-R), floor(X+R)+1)

# cnt = 0
# for x in range(ceil(X-R), floor(X+R)+1):
#     w = abs(x - X)
#     h = square_root(R**2 - w**2)
#     cnt += floor(Y+h) - ceil(Y-h) + 1

# print(cnt)
