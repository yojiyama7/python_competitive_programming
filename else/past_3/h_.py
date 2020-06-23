from itertools import accumulate as acc

N, L = map(int, input().split())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

th = [t//2 for t in T]

tj = th[0]+th[1]
jump1 = list(acc([0, tj, tj]))
jump2 = list(acc([0, tj, T[1], T[1], tj]))

hurdle = [0]*(L+1)
for x in X:
    hurdle[x] = 1

dp = [10**18]*(L+1)
dp[0] = 0
for i in range(L):
    is_hurdle = hurdle[i]
    dp[i+1] = min(
        dp[i+1],
        dp[i] + T[0] + T[2]*is_hurdle
    )
    dp[min(i+2, L)] = min(
        dp[min(i+2, L)],
        dp[i] + jump1[min(L-i, 2)] + T[2]*is_hurdle
    )
    dp[min(i+4, L)] = min(
        dp[min(i+4, L)],
        dp[i] + jump2[min(L-i, 4)] + T[2]*is_hurdle
    )

print(dp[L])