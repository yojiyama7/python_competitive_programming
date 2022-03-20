N = int(input())

sum_num = 0
for i in range(1, N+1):
    x = N//i
    m = (x*(x+1) // 2) * i
    sum_num += m

print(sum_num)

################################

# N = int(input())

# def solve():
#     def f(x):
#         if x == 1:
#             return 1
#         count = 0
#         for i in range(1, int(x*(1/2))+2):
#             if i**2 > x:
#                 break
#             elif i**2 == x:
#                 count += 1
#             elif x%i == 0:
#                 count += 2
#         return count

#     # [print(f(k)) for k in range(1, N+1)]

#     r = sum(k * f(k) for k in range(1, N+1))
#     print(r)