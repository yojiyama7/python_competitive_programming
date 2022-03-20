MOD = 998244353

N, K, M = map(int, input().split())
# Aの通り数 = K**N
# 答え = M**(K**N)
# フェルマーの小定理

# これ忘れるのどうにかならんの
if M%MOD == 0:
    ans = 0
else:
    ans = pow(M, pow(K, N, MOD-1), MOD)
print(ans)
