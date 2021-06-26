# https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d

# これ偉いな
# O(DN) じゃない？
# 洋服は派手さが最大化最小のほうがいい と。

D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
ABC = [list(map(int, input().split())) for _ in range(N)]

A, B, C = zip(*ABC)

dp = [dict() for _ in range(D+1)]
# dp[0][0] = 0
for i, t in enumerate(T, start=1):
    min_c = 101
    max_c = -1
    for a, b, c in ABC:
        if a <= t <= b:
            min_c = min(min_c, c)
            max_c = max(max_c, c)
    dp[i][min_c] = 0
    dp[i][max_c] = 0
    if i == 1:
        continue
    for k, v in dp[i-1].items():
        dp[i][min_c] = max(
            v + abs(k - min_c),
            dp[i][min_c]
        )
        dp[i][max_c] = max(
            v + abs(k - max_c),
            dp[i][max_c]
        )

# print(dp)

print(max(dp[D].values()))

################################

# INF = float('inf')

# D, N = map(int, input().split())
# T = [int(input()) for _ in range(D)]
# ABC = [list(map(int, input().split())) for _ in range(N)]

# max_score = [0]*D
# min_score = [INF]*D
# for i, t in enumerate(T):
#     for a, b, c in ABC:
#         if a <= t <= b:
#             max_score[i] = max(
#                 c,
#                 max_score[i],
#             )
#             min_score[i] = min(
#                 c,
#                 min_score[i],
#             )

# ans1 = 0
# b = max_score[0]
# # print(b)
# for i in range(1, D):
#     if i%2:
#         c = min_score[i]
#     else:
#         c = max_score[i]
#     # print(c)
#     ans1 += abs(c-b)
#     b = c
# # print(">>>", ans1)

# ans2 = 0
# b = min_score[0]
# # print(b)
# for i in range(1, D):
#     if i%2 == 0:
#         c = min_score[i]
#     else:
#         c = max_score[i]
#     # print(c)
#     ans2 += abs(c-b)
#     b = c
# # print(">>>", ans2)

# ans = max(ans1, ans2)
# print(ans)
