# dp ですかそうですか
# 雰囲気を感じ取れませんでした

from collections import Counter

MOD = 998244353

S = input()

values = list(Counter(S).values())

fact = [None]*5001
fact[0] = 1
inv = [None]*5001
inv[0] = 1
for i in range(1, 5001):
    fact[i] = (fact[i-1] * i) % MOD
    inv[i] = pow(fact[i], MOD-2, MOD)

# len(S) 文字の時
ans = fact[sum(values)]
for v in values:
    ans *= inv[v]
print(ans)


# ans = 0
# for i in range(1, len(S)+1):
#     score = fact[len(S)] * inv[len(S)-i]
#     score %= MOD
#     ans += score
#     ans %= MOD

# print(ans)
