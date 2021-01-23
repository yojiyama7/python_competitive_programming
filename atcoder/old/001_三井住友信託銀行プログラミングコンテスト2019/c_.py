X = int(input())

a, b = X//100, X%100

if -(-b//5) <= a:
    print("1")
else:
    print("0")

# # i個の商品でj円(下2桁)を作れるか
# dp = [[0 for j in range(b+1)] for i in range(a+1)]

# dp[0][0] = 1

# for i in range(a):
#     for j in range(b):
#         if dp[i][j] == 0:
#             continue
#         for k in range(j, min(b+1, j+6)):
#             dp[i+1][k] = 1

# print(dp)

# if dp[a][b]:
#     print(1)
# else:
#     print(0)