MOD = 10**9+7

N = int(input())

def h_mod(n, k):
	return c_mod(n+k-1, k-1)

fact = [1]*(N+1)
fact_inv = [1]*(N+1)
for i in range(1, N+1):
	fact[i] = fact[i-1]*i
	fact[i] %= MOD
	fact_inv[i] = pow(fact[i], MOD-2, MOD)

def c_mod(n, k):
	x = fact[n]
	x *= fact_inv[n-k]
	x %= MOD
	x *= fact_inv[k]
	x %= MOD
	return (x)

l = [0]*N
# k: 選ぶ個数
for k in range(1, N+1):
	# x: 隙間の大きさ
	for x in range(N):
		locked = k + x*(k-1)
		if not (locked <= N):
			break
		remain = N-locked
		l[x] += h_mod(remain, k+1)
		l[x] %= MOD

print(*l, sep="\n")
