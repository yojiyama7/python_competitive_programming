# 理屈は正しいけどpythonの弱さ

def main():
    MOD = 998244353

    N, M, K = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]

    g = [set() for i in range(N)]
    for u, v in UV:
        u -= 1
        v -= 1
        g[u].add(v)
        g[v].add(u)

    # i日目 に j にいるときのパターン数
    dp = [[0 for j in range(N)] for i in range(K+1)]
    dp[0][0] = 1
    # dp2[i]: dp[i][x](0 <= x < N)
    dp2 = [0 for i in range(K+1)]
    dp2[0] = 1

    for i in range(1, K+1):
        for j in range(N):
            # dp[i-1][x](x: jと連結な都市)
            # dp[i-1][x](0 <= x < N) - dp[i-1][y](y: jと非連結な都市)
            # dp2[i-1] - dp[i][y]=
            # print((i, j), dp2[i-1], sum(dp[i-1][to] for to in g[j]))
            dp[i][j] = dp2[i-1] - dp[i-1][j] - sum(dp[i-1][to] for to in g[j])
            dp[i][j] %= MOD
            dp2[i] += dp[i][j]
            dp2[i] %= MOD

    # print(dp)

    print(dp[K][0])

main()
