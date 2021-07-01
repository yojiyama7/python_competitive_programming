# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp

import sys

input = sys.stdin.readline
write = sys.stdout.write
INF = float('inf')

def clamp(a, x, b):
        if x < a:
            return a
        elif a <= x <= b:
            return x
        else:
            return b

cost = [[(i-j)**2 for j in range(256)] for i in range(256)]

def solve():
    N, M = map(int, input().split())
    if N == M == 0:
        return False
    print([N, M])
    C = [int(input()) for _ in range(M)]
    X = [int(input()) for _ in range(N)]

    # Yi を j にするとき取れるスコア最小値
    dp = [[INF for j in range(256)] for i in range(N+1)]
    dp[0][128] = 0
    j_jc_set = set()
    for j in range(256):
        for c in C:
            x = (j, clamp(0, j+c, 255))
            j_jc_set.add(x)

    for i, Xi in enumerate(X):
        # if i % 500 == 0:
        #     print(i, end='\r', flush=True)
        cost_Xi = cost[Xi]
        for j, jc in j_jc_set:
            score = dp[i][j] + cost_Xi[j]
            if dp[i+1][jc] > score:
                dp[i+1][jc] = score
        # for j in range(256):
        #     for c in C:
        #         x = clamp(0, j+c, 255)
        #         score = dp[i][j] + cost[Xi][j]
        #         if dp[i+1][x] > score:
        #             dp[i+1][x] = score
                # dp[i+1][x] = min(
                #     dp[i][j] + (X[i]-x)**2,
                #     dp[i+1][x]
                # )
    print()
    # for dp_i in dp:
    #     print([[j, dp_ij] for j, dp_ij in enumerate(dp_i) if dp_ij != INF])
    write("%s\n" % min(dp[N]))
    return True

while solve():
    ...
