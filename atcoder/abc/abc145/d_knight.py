X, Y = map(int, input().split())

MOD = 10**9+7

# コピペ

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range(2, 10**6+1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)

def combi_mod(n, r):
    if (r<0 or r>n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % MOD

# ====

sum_num = 0
for n in range(X+1):
    x, y = 1*n, 2*n
    xr, yr = X-x, Y-y
    if xr == yr*2:
        m = yr
        sum_num = (sum_num + combi_mod(n+m, m)) % MOD

print(sum_num)

