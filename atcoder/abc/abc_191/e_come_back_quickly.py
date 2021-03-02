INF = 0

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

g = [[INF for _ in range(N)] for _ in range(N)]
for a, b, c in ABC:
    g[a][b] = min(g[a][b], c)

