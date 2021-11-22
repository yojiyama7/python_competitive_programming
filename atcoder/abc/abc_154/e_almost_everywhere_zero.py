# 配るdp, 桁dp

N = input()
K = int(input())

N_len = len(N)

# dp[i][j][sm]: i文字目までXとしたとき、X[と等しい, 未満の][sm]数で、0でない数がj個あるパターン
dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(N_len+1)]
dp[0][0][0] = 1
for i, n in enumerate(N):
    n = int(n)
    for j in range(K+1):
        for k in range(10):
            if k == n:
                if j+(k!=0) <= K:
                    dp[i+1][j+(k!=0)][0] += dp[i][j][0]
            elif k < n:
                if j+(k!=0) <= K:
                    dp[i+1][j+(k!=0)][1] += dp[i][j][0]

            if j+(k!=0) <= K:
                dp[i+1][j+(k!=0)][1] += dp[i][j][1]

ans = sum(dp[N_len][K])
print(ans)

################################

# N = input()
# K = int(input())

# n = list(map(int, "{0:0<102}".format(N)))

# # def solve(N, K, smaller):

################################

# N = input()
# K = int(input())

# n = "{0:0<101}".format(N)

# print(n)

# # 上からi桁目までで、0以外の文字をj個ふくんだ物の数(k==0の時それ以降はnより下で遷移、k==1の時は0-9で遷移)
# dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(101)]
# dp[0][0][0] = 1

# for i in range(100):
#     a = int(n[i])
#     for j in range(a):
#         if j == 0:
#             dp[i+1][0][1] += dp[i][0][1]
#             dp[i+1][1][1] += dp[i][1][1] 
#             dp[i+1][2][1] += dp[i][2][1]
#             dp[i+1][3][1] += dp[i][3][1]
