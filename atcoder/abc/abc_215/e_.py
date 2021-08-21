# i番目までのコンテストで
# すでにA~Jのうち j(ビット列) のコンテストには出た状態で
# 前回選んだのがkで
# あるときのパターン数
MOD = 998244353

N = int(input())
S = input()

S_id = [ord(s) - ord('A') for s in S]
dp = [[[0 for k in range(11)] for j in range(1<<10)] for i in range(N+1)]
dp[0][0][-1] = 1
for i, s_id in enumerate(S_id):
    for j in range(1<<10):
        for k in range(11):
            dp[i+1][j][k] += dp[i][j][k]
            dp[i+1][j][k] %= MOD
            if (j>>s_id)&1 == 0 or s_id == k:
                dp[i+1][j|(1<<s_id)][s_id] += dp[i][j][k]
                dp[i+1][j|(1<<s_id)][s_id] %= MOD
# print(*dp, sep='\n')
# for i in range(N+1):
#     cnt = 0
#     for j in range(1<<10):
#         cnt += sum(dp[i][j])
#         if sum(dp[i][j]):
#             print(bin(j)[2:], sum(dp[i][j]))
#     print(i, "???", cnt)
ans = 0
for j in range(1, 1<<10):
    ans += sum(dp[N][j])
    ans %= MOD
print(ans)

################################

# N = int(input())
# S = input()

# S_id = [ord(s) - ord('A') for s in S]
# dp = [[0 for j in range(1<<10)] for i in range(N+1)]
# dp[0][0] = 1
# for i, s_id in enumerate(S_id):
#     for j in range(1<<10):
#         dp[i+1][j] += dp[i][j]
#         if j>>s_id
#             dp[i+1][j | (1<<s_id)] += dp[i][j]
