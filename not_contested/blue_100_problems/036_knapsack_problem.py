# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja

N, W = map(int, input().split())
VW = [list(map(int, input().split())) for _ in range(N)]

# 各品物を遷移にする なるほどね

dp = [0 for _ in range(W+1)]
for i in range(1, W+1):
    # dp[i] = dp[i-1]
    for v, w in VW:
        if i-w >= 0:
            dp[i] = max(
                dp[i-w] + v,
                dp[i]
            )

# print(dp)
print(dp[W])
