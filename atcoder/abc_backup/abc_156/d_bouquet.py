# X/Y mod(10**9+7) == X*(Y**(10**9+7-2)) mod(10**9+7)

MOD = 10**9+7

def mod_prod(l, mod=MOD):
    p = 1
    for x in l:
        p = (p * x) % mod
    return p

n, *ab = list(map(int, input().split()))

count = pow(2, n, MOD) - 1
# print(count)

for k in ab:
    # print(f"k: {k}")
    x = mod_prod(range(n-k+1, n+1))
    y = mod_prod(range(1, k+1))
    z = x * pow(y, MOD-2, MOD)
    # print(z)
    count = (count - z) % MOD

print(count)

