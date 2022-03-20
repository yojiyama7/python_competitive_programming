# 無向重みありグラフを構築できれば巡回セールスマン問題
# 幅優先*Kでできる

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C = list(map(int, input().split()))

g = [set() for _ in range(N)]

for a, b in AB:
    a, b = a-1, b-1
    g[a].add(b)
    g[b].add(a)

small_g = [[INF for _ in range(K)] for _ in range(K)]
for i in range(K):
    small_g[i][i] = 0:
    

################################

# INF = float("inf")

# N, M = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]
# K = int(input())
# C = list(map(int, input().split()))

# g = [set() for _ in range(N)]

# for a, b in AB:
#     a, b = a-1, b-1
#     g[a].add(b)
#     g[b].add(a)

# dp = [[INF for _ in range(N)] for _ in range(1<<K)]
# dp[0][0] = 0
# def solve(bit, v):
#     if bit == 0:
#         return (INF if v else 0)
#     if bit & (1<<v) == 0:
#         return (INF)
#     print("SO")
#     if dp[bit][v] == INF:
#         for u in g[v]:
#             dp[bit][v] = min(
#                 dp[bit][v],
#                 solve(bit ^ (1<<u), u) + 1
#             )
#     return dp[bit][v]

# print(*dp, sep="\n")

# ans = solve((1<<K)-1, 0)
# print(-1 if ans == INF else ans)