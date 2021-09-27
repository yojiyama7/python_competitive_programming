################################

# # NO SUB

# MOD = 998244353

# N, D = map(int, input().split())

# ans = 0
# for i in range(N):
#     a_max = min(D, N-i-1)
#     a_min= max(0, D - a_max)

#     if a_min > a_max:
#         break
#     ans += (a_max-a_min+1) * pow(2, D, MOD)
#     ans %= MOD
#     print(i, (a_min, a_max), ans)

# print(ans)

################################

# ans = 0
# for i in range(N-D):
#     ans += pow(2, i+D, MOD)

# print(ans)

# for a in range(1, D):
#     b = D-a
#     x = pow(2, a-1, MOD)
#     y = pow(2, b-1, MOD)
#     ans += x*y
#     ans %= MOD
#     print((a, b), ans)

# print(ans)