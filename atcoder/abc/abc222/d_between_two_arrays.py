MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for j in range(3001)] for i in range(N)]
memo = [[0 for j in range(3001)] for i in range(N)]
for j in range(3001):
    if A[0] <= j <= B[0]:
        dp[0][j] = 1
    memo[0][j] = dp[0][j]
    if j-1 >= 0:
        memo[0][j] += memo[0][j-1]
        memo[0][j] %= MOD

for i in range(1, N):
    a, b = A[i], B[i]
    for j in range(3001):
        if a <= j <= b:
            dp[i][j] = memo[i-1][j]
        memo[i][j] = dp[i][j]
        if j-1 >= 0:
            memo[i][j] += memo[i][j-1]
            memo[i][j] %= MOD

# [print(dp_i[:20]) for dp_i in dp]
# [print(memo_i[:20]) for memo_i in memo]

print(memo[N-1][3000])