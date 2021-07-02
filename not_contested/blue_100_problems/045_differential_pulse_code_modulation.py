# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp

# main で囲っただけで通ったんですがどういうこと
# グローバル変数の参照が遅いみたいなのでmainを作るとよいとのこと　は？
import sys

def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    INF = float('inf')

    cost = tuple(tuple((i-j)**2 for j in range(256)) for i in range(256))

    while True:
        N, M = map(int, readline().split())
        if N == M == 0:
            break
        # print(N, M)
        C = tuple(int(readline()) for _ in range(M))
        X = tuple(int(readline()) for _ in range(N))

        p = set()
        for j in range(256):
            for c in C:
                if j+c < 0:
                    to = 0
                elif j+c > 255:
                    to = 255
                else:
                    to = j+c
                p.add((to, j))
        dp = [INF]*256
        dp[128] = 0
        for x in X:
            dp2 = list(dp)
            dp = [INF]*256
            cost_x = cost[x]
            for to, j in p:
                c = dp2[j] + cost_x[to]
                if c < dp[to]:
                    dp[to] = c
        print(min(dp))

if __name__ == '__main__':
    main()

################################

# import sys

# readline = sys.stdin.readline
# write = sys.stdout.write
# INF = 10**18

# def clamp(a, x, b):
#         if x < a:
#             return a
#         elif a <= x <= b:
#             return x
#         else:
#             return b

# cost = [[(i-j)**2 for j in range(256)] for i in range(256)]

# ans_list = []
# while True:
#     N, M = map(int, readline().split())
#     if N == M == 0:
#         break
#     # print([N, M])
#     C = [int(readline()) for _ in range(M)]
#     X = [int(readline()) for _ in range(N)]

#     p = [set() for j in range(256)]
#     for j in range(256):
#         for c in C:
#             to = clamp(0, j+c, 255)
#             # print(j, jc)
#             p[to].add(j)
#     dp = [[INF for j in range(256)] for i in range(N+1)]
#     dp[0][128] = 0
#     for i, (x, dp_i) in enumerate(zip(X, dp)):
#         # print([dp_i for i, dp_i in enumerate(dp) if dp_i != INF])
#         if i % 500 == 0:
#             print(i, end='\r', flush=True)
#         # dp2 = [INF for j in range(256)]
#         # cost_x = cost[x]
#         for to, js in enumerate(p):
#             dp[i+1][to] = min((dp_i[j] + cost[x][to] for j in js), default=INF)
#         # dp = dp2[:]
#         # for j in range(256):
#         #     for c in C:
#         #         x = clamp(0, j+c, 255)
#         #         score = dp[i][j] + cost[Xi][j]
#         #         if dp[i+1][x] > score:
#         #             dp[i+1][x] = score
#                 # dp[i+1][x] = min(
#                 #     dp[i][j] + (X[i]-x)**2,
#                 #     dp[i+1][x]
#                 # )
#     print()
#     # for dp_i in dp:
#     #     print([[j, dp_ij] for j, dp_ij in enumerate(dp_i) if dp_ij != INF])
#     ans_list.append(min(dp[N]))

# for ans in ans_list:
#     write("%s\n" % ans)

