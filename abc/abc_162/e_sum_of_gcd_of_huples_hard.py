MOD = 10**9+7

N, K = map(int, input().split())

# 1-indexed
l = [0]*(K+1)
for i in range(1, K+1):
    p = pow(K//i, N, MOD)
    l[i] = p

for i in range(K, 0, -1):
    for j in range(2*i, K+1, i):
        l[i] = (l[i] - l[j]) % MOD

r = 0
for i, l_i in enumerate(l):
    r = (r + (i*l_i) % MOD) % MOD

print(r)