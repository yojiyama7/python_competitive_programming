# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja

INF = float('inf')

N, M = map(int, input().split())
C = list(map(int, input().split()))

# dp[i]: i円を払うために必要な最小枚数
dp = [INF for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    for c in C:
        if i-c >= 0:
            dp[i] = min(
                dp[i-c] + 1,
                dp[i]
            )

# print(dp)
print(dp[N])
