N = int(input())
T = list(map(int, input().split()))

T_1idx = [None] + T
T_sum = sum(T)

# print(T_sum)

limit = T_sum//2
dp = [[0 for _ in range(limit+1)] for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    t = T_1idx[i]
    for j in range(limit+1):
        # if i == 2 and j == 11:
        #     print("aaa", t)
        dp[i][j] |= dp[i-1][j]
        if j >= t:
            # if dp[i-1][j-t]:
            #     print(i, j, t)
            dp[i][j] |= dp[i-1][j-t]

# [print(dp_i) for dp_i in dp]

a = None
for i in reversed(range(limit+1)):
    if dp[N][i]:
        a = i
        break
# print(a)

ans = max(a, T_sum-a)
print(ans)
