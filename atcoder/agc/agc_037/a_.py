S = input()
n = len(S)

# Sのi番目を最後尾として、j文字をとったときの最大のK
dp = [[0, 0, 0] for _ in range(n)]
dp[0][1] = 1
dp[0][2] = -(10**18)
dp[1][1] = 1

# i: 0-indexted
for i in range(1, n):
    # print(f"i: {i}")
    if S[i-1] == S[i]:
        dp[i][1] = dp[i-1][2]+1
    else:
        dp[i][1] = max(
            dp[i-1][1]+1,
            dp[i-1][2]+1
        )
    end = i+1
    if S[max(0, end-4):max(0, end-2)] == S[max(0, end-2):end]:
        dp[i][2] = dp[i-2][1]+1
    else:
        dp[i][2] = max(
            dp[i-2][1]+1,
            dp[i-2][2]+1
        )
    # for dp_i in dp:
    #     print(dp_i)

print(max(dp[n-1]))
