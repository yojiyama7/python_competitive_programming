# 加算と減算なので順番を入れ替えることができる
# ある数がmaxになるパターン数 * ある数 分のプラス
# ある数がminになるパターン数 * ある数 分のマイナス
# を別に考える

# 自分が小さい方からx番目(1-indexed)の時、
# maxになるパターン数は、(x-1)C(K-1)

# 自分が大きい方からy番目(1-indexed)の時、
# minになるパターンは、(y-1)C(K-1)

# ↓これ理解したい。(フェルマーの小定理を利用した mod_combination)
MOD = 10**9+7

n = 10**5
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル
for i in range(2, n+1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)

def combi(n, r):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % MOD

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

result = 0
for i, a in enumerate(A):
    s = combi(i, K-1)*a
    result = (result + s) % MOD

for i, a in enumerate(A[::-1]):
    s = combi(i, K-1)*a
    result = (result - s) % MOD

print(result)