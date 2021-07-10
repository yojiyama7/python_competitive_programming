INF = 10**18

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

cost = [[INF for j in range(N)] for i in range(N)]
for i in range(N):
    cost[i][i] = 0
for a, b, c in ABC:
    a -= 1
    b -= 1
    cost[a][b] = c

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] == INF or cost[k][j] == INF:
                continue
            cost[i][j] = min(
                cost[i][j],
                cost[i][k] + cost[k][j]
            )
    for i in range(N):
        for j in range(N):
            if cost[i][j] == INF:
                continue
            ans += cost[i][j]

print(ans)
