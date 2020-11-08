N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

INF = float("inf")
# 探索済みノードがj(bit set)で現在iにいる
dp = [[INF]*(1<<N) for _ in range(N)]
dp[0][0] = 0
