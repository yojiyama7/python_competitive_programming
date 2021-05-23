# 2項係数(MOD 素数)ですって奥さん。
# 数学やってこい    

################################

# from math import factorial as f

# N, M = map(int, input().split())
# # M = 10**9

# MOD = 10**9+7

# # √M+1未満の素数を生成 O(√M*Mまでの素数の個数) 1億オーダーぐらい?、辛い
# # primes = [2]
# # for i in range(3, 31608):
# #     if all(i%prime != 0 for prime in primes):
# #         primes.append(i)

# d = [0]*4000
# for i, prime in enumerate(primes):
#     while M % prime == 0:
#         M //= prime 
#         d[i] += 1

# count = 1
# for d_i in d:
#     if d_i == 0:
#         continue
#     count = (combi(M+N-1, N-1) // f(N-1) * count) % MOD

# print(count)