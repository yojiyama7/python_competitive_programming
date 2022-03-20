################################
# これでACしましたがTにまとめるのでダメなのはなぜ

N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()
# N, T = 3000, 14
# AB = [(i**2, i) for i in range(N)]

# dp[i+1][j] = i番目までの料理で、j分経った時の、最高満足度
# jがT以上のときはj == T とする(T以上における差はないので)

dp = [[0 for _ in range(6010)] for _ in range(3010)]

max_num = 0
for i, (a, b) in enumerate(AB):
    # print(a, b)
    for j in range(T):
        if j == T-1:
            max_num = max(
                max_num,
                dp[i][j] + b
            )
        dp[i+1][j] = max(
            dp[i+1][j],
            dp[i][j]
        )
        dp[i+1][j+a] = max(
            dp[i+1][j+a],
            dp[i][j] + b
        )

# for dp_i in dp:
#     print(dp_i)

print(max_num)
