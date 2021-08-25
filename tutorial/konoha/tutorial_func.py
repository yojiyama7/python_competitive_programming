# # def: [de]fine [f]ucntion

# def add_mul(a, b):
#     return (a+b, a*b)

# def my_sum(l):
#     ans = 0
#     for li in l:
#         ans += li
#     return ans

# def print_more(x):
#     print("----------")
#     print("value:", x)
#     print("type :", type(x))
#     # print("dir  :", dir(x))
#     print("----------")

# A = 10
# B = 20
# # L = list(range(100))
# # print(L)

# # # print(add_mul(A, B))
# # print(my_sum(L))

# print_more(A)
# print_more("9283hdsjas")
# print_more([1, 2, 4, 23, 323])

# # x = 1
# # print(x.bit_length())

# N = int(input())

# def solve():
#     for i in range(1, 10):
#         for j in range(1, 10):
#             if i*j == N:
#                 return "Yes"
#     return "No"

# print(solve())

# def my_min(a, *args):
#     ans = a
#     for x in args:
#         if x < ans:
#             ans = x
#     return ans

# print(my_min(4))
# print(my_min(4, 2))
# print(my_min(4, 2, 1))
# print(my_min(4, 2, 1, 5))
# print(my_min())



# def my_all(l):
#     for li in l:
#         if li:
#             continue
#         return False
#     return True

# def my_any(l):
#     for li in l:
#         if li:
#             return True
#     return False

# a = 12
# l = [a%3 == 0, a%5 != 0]
# if my_all(l):
#     print("Yes")
# else:
#     print("No")

# if my_any