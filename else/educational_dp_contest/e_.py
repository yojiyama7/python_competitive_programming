from bisect import bisect_right

N, W = map(int, input().split(" "))
WV = [list(map(int, input().split(" "))) for _ in range(N)]

# i番目までで、価値jに必要な最小の重さ
dp = [10**18 for _ in range(N*1000)]

# print(dp[0][0])
for i, (w, v) in enumerate(WV):
    dp[i+1] = 
