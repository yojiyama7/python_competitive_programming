# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d

INF = float("inf")

N = int(input())
S = [input() for _ in range(5)]

cost = [[0 for _ in range(3)] for _ in range(N+1)]

for i, s in enumerate(zip(*S), start=1):
    for c in s:
        col = "RBW#".find(c)
        for x in range(3):
            if x == col:
                continue
            cost[i][x] += 1

dp = [[INF for j in range(4)] for i in range(N+1)]
dp[0][3] = 0

for i in range(1, N+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][x] + cost[i][j] for x in range(4) if x != j)

print(min(dp[N]))
