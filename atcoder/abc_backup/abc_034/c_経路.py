from math import factorial as f

W, H = map(int, input().split(" "))

print(f(W+H-2)*pow(f(W-1)*f(H-1), 10**9+7-2, 10**9+7)%(10**9+7))

################################

# # TLE

# from math import factorial as f

# W, H = map(int, input().split(" "))

# print(f(W+H-2)//f(H-1)//f(W-1)%(10**9+7))

################################

# W, H = map(int, input().split(" "))

# W, H = W-1, H-1
# a = W+H

# m = 1
# for i in range(a, W, -1):
#     print(i)
#     m = (m*i)%(10**9+7)

# print(m)

################################

# 逆元 フェルマーの小定理 よくわからん
# 解説 https://www.slideshare.net/chokudai/abc034
# やっぱわからん 多分ここに全てが詰まってる
# https://gyazo.com/564e9ac1b37a4c87c9502fa4cd5ccd8d

# # WA

# from math import factorial

# W, H = map(int, input().split(" "))

# a = W+H-2
# num = 1
# for i in range(min(W-1, H-1)):
# 	num = (num*a)

# a = (a*b)%(10**9+7)
