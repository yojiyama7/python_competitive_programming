MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# N = 5000
# A = list(range(1, 5001))
# B = list(range(1, 5001))

AB = list(zip(A, B))
AB.sort()
# A, B = zip(*AB)
# print(A, B)

ans = 0

dp = [[0 for j in range(5001)] for i in range(N+1)]
dp[0][0] = 1
for i, (a, b) in enumerate(AB, start=1):
    dp_ineg1 = dp[i-1]
    # print(i)
    for j in range(5001):
        dp[i][j] += dp_ineg1[j]
        dp[i][j] %= MOD
        if j >= b:
            dp[i][j] += dp_ineg1[j-b]
            dp[i][j] %= MOD
    # print(i, (a, b), dp[i][1:a+10])
    for x in dp[i][1:a+1]:
        ans += x
        ans %= MOD
    for x in dp_ineg1[1:a+1]:
        ans -= x
        ans %= MOD

print(ans)
