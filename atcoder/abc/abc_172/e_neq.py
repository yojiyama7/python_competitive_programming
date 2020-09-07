################################

# # NOT AC

# MOD = 10**9+7

# N, M = map(int, input().split())

# a = [1 for i in range(N+1)]
# b = [1 for i in range(N+1)]
# for i in range(N):
#     a[i+1] = (a[i] * ((M-i)%MOD)) % MOD
#     b[i+1] = (((b[i]-i)%MOD) * ((M-(i+1))%MOD) + (M-i)%MOD*i) % MOD
#     # print(i, [(b[i]-1),  (M-(i+1))], (M-i))

# # print(a, b)

# r = (a[N] * b[N]) % MOD
# print(r)