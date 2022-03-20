from itertools import chain

INF = 10**18

H, W = map(int, input().split())
C = [input() for _ in range(H)]

dp = [[-INF for _ in range(W)] for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == j == 0:
            continue
        if C[i][j] == '#':
            continue
        before_max = -INF
        if i-1 >= 0 and C[i-1][j] == '.':
            before_max = max(before_max, dp[i-1][j])
        if j-1 >= 0 and C[i][j-1] == '.':
            before_max = max(before_max, dp[i][j-1])
        dp[i][j] = before_max + 1

# print(*dp, sep='\n')

ans = max(chain(*dp))
print(ans)