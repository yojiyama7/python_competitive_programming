# v個の同じ商品をn個のそれぞれ別の番号のついた箱に入れるパターン数
# -> v個の品(区別しない), n個の箱(区別する)
# -> v個の 'o' と (n-1)個の '/' を並べた時にできる文字列のパターン数と等しい
# -> v + n-1 C v (文字数のうち v 文字を 'o' として選ぶパターン('/'は自ずと決まる))
# (v+n-1 C v) となる
# またこれを、 (n H v) と表す(順番に注意)
# (n H v) はn種類の品を重複を許してv個選ぶパターン数

MOD = 10**9+7

N, M = map(int, input().split())

# Mの素因数分解
d = dict()
num = M
x = 2
while num > 1 and x**2 <= M:
	while num%x == 0:
		if x not in d:
			d[x] = 0
		d[x] += 1
		num //= x
	x += 1
if num > 1:
	d[num] = 1

f = [1]
f_inv = [1]
for i in range(1, N+100):
	f_i = f[-1]*i
	f_i %= MOD
	f.append(f_i)
	f_inv_i = pow(f_i, MOD-2, MOD)
	f_inv.append(f_inv_i)
# print(f)
# print(f_inv)

# n <= 10**5, k <= 30
def combi(n, k):
	if n < k:
		return 0
	return (f[n]*f_inv[k] %MOD)*f_inv[n-k] %MOD

# 品i(種類数<=30)がd[i]個ある
# これらをNグループに分割する
# -> 各種類をNグループに分割するパターンの総積
# d[i]個をNグループに分割する(グループの大きさは0でもよい)
# -> d[i]+1個の区切り候補をN-1回選ぶ == (d[i]+1)**(N-1)
# FIX: 上記では、各区切り候補に入った区切りの数が等しいパターンを重複してカウントしている
# print(d)
ans = 1
for v in d.values():
	# print(N+v-1, v, combi(N+v-1, v))
	ans *= combi(N+v-1, v)
	ans %= MOD
print(ans)

################################

# # 2項係数(MOD 素数)ですって奥さん。
# # 数学やってこい

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