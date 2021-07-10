import re

N = int(input())

memo = dict()


def is_agc(text):
    if re.match("(.agc|.acg|.gac|a.gc|ag.c)", text):
        return True
    return False


def dfs(s, m):
    if (s, m) in memo:
        return memo[(s, m)]
    if m == N:
        return 1

    count = 0
    for c in "acgt":
        t = s + c
        if is_agc(t):
            continue
        count += dfs(t[-3:], m+1)

    # print(s, m, count)
    memo[(s, m)] = count % (10**9+7)
    return memo[(s, m)]


print(dfs("ttt", 0))
# print(memo)

################################

# N = int(input())

# # dp[i][j] = i番目が文字j
# dp = [[0]*4 for _ in range(N+1)]
# dp[1] = [1]*4
# dp[2] = [4]*4
# for i in range(3, N+1):
#     dp[i][0] = sum(dp[i-1])
#     dp[i][1] = sum(dp[i-1]) - (dp[i-1][0] - sum(dp[i-2]) + )

# print(dp)
# print(sum(dp[N]))
