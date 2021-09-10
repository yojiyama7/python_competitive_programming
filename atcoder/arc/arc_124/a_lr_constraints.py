from itertools import accumulate as acc

MOD = 998244353

N, K = map(int, input().split())
CK = [input().split() for _ in range(K)]

CK = [(c, int(k)-1) for c, k in CK]

locked = [None]*N
for i, (c, k) in enumerate(CK):
    locked[k] = i
l = [0]*(N+1)
for i, (c, k) in enumerate(CK):
    if c == 'L':
        l[k+1] += 1
        l[N] -= 1
    else:
        l[0] += 1
        l[k] -= 1
l_acced = list(acc(l))[:N]

ans = 1
for i, li in enumerate(l_acced):
    if locked[i] != None:
        continue
    ans *= li
    ans %= MOD

print(ans)
