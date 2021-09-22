MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

cnt = [[0 for _ in range(2)] for i in range(N)]
cnt[0][0] = 1
dp = [[0 for _ in range(2)] for i in range(N)]
dp[0][0] = A[0]
for i in range(1, N):
    cnt[i][0] = sum(cnt[i-1])
    cnt[i][0] %= MOD
    cnt[i][1] = cnt[i-1][0]
    cnt[i][1] %= MOD
    dp[i][0] = sum(dp[i-1]) + A[i]*cnt[i][0]
    dp[i][0] %= MOD
    dp[i][1] = dp[i-1][0] - A[i]*cnt[i][1]
    dp[i][0] %= MOD

# print(cnt)
# print(dp)

ans = sum(dp[N-1])
ans %= MOD

print(ans)
