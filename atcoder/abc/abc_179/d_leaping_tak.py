# もうちょっと細かく詰めるbeki

N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]

rngs = [(l, r+1) for l, r in LR]

dp = [0]*N
dp_acc = [0]*(N+1)
dp[0] = 1
dp_acc[0] = 1
for i in range(1, N):
    for rng in rngs:
        l, r = max(0, i - rng[0]), max(0, i - rng[1])
        print(l, r, dp_acc[r] - dp_acc[l])
        dp[i] += dp_acc[r] - dp_acc[l]
    dp_acc[i] = dp_acc[i-1] + dp[i]

print(dp, dp_acc)

print(dp[N-1])