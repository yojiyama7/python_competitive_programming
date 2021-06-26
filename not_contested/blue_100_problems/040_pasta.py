# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d

MOD = 10000

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(K)]

l = [0]*(N+1)
for a, b in AB:
    l[a] = b

dp = [[[0 for k in range(4)] for j in range(4)] for i in range(N+1)]
dp[0][0][0] = 1

for i in range(1, N+1):
    p = [l[i]] if l[i] else range(1, 4)
    for j in p:
        for k in range(4):
            for x in range(4):
                if j == k == x:
                    continue
                dp[i][j][k] += dp[i-1][k][x]

ans = 0
for j in range(1, 4):
    for k in range(1, 4):
        ans += dp[N][j][k]
        ans %= MOD

print(ans)
