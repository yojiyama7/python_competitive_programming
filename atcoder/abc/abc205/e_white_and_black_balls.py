# カタラン数
# 組み合わせ(a+bCa) を グリッド(a*b) での 移動経路として捉えるのはありがち

MOD = 10**9+7

N, M, K = map(int, input().split())

if N > M+K:
    print(0)
    exit()

t = ""
# t += '0'*K
t += '1'*K
t += "01"*(N-K)
t += '0'*(M-N)

print(t)
t = t[::-1]
print(t)

ans = 1
cnt = 0
for i, t_i in enumerate(t):
    if t_i == '0':
        continue
    p = i-cnt+1
    print(p)
    ans *= p
    ans %= MOD
    cnt += 1
    # print(ans)

print(ans)