INF = float('inf')
MOD = 998244353

H, W, K = map(int, input().split())
HWC = [input().split() for _ in range(K)]

m = [[0 for _ in range(W)] for _ in range(H)]
for y, x, c in HWC:
    x, y = int(x)-1, int(y)-1
    m[y][x] = " RDX".index(c)

dp = [[[0 for _ in range(3)] for _ in range(W)] for _ in range(H)]
[print(m_i) for m_i in m]

if m[0][0] == 0:
    for i in range(3):
        dp[0][0][i] = 1
else:
    dp[0][0][m[0][0]-1] = 1

# [print(dp_i) for dp_i in dp]

for y in range(H):
    for x in range(W):
        if x == y == 0:
            continue
        val = 0
        if y >= 1:
            val += dp[y-1][x][1] + dp[y-1][x][2]
            val %= MOD
        if x >= 1:
            val += dp[y][x-1][0] + dp[y][x-1][2]
            val %= MOD
        if m[y][x] == 0:
            dp[y][x][0] = val
            dp[y][x][1] = val
            dp[y][x][2] = val
        else:
            dp[y][x][m[y][x]-1] = val

[print(dp_i) for dp_i in dp]

print(sum(dp[H-1][W-1][i] for i in range(3)))