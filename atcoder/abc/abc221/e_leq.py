MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

t = sorted(set(A))
d = dict(zip(t, range(len(t))))

p = [d[a] for a in A]

print(p)

################################

# ans = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if A[i] > A[j]:
#             continue
#         ans += pow(2, j-i-1, MOD)
#         ans %= MOD

# print(ans)

################################

# dp = [[0 for _ in range(2)] for i in range(N+1)]
# for i, a in enumerate(A):
#     dp[i+1][0] = sum(dp[i]) * 2
#     dp[i+1][0] %= MOD
#     dp[i+1][1] = dp[i][1] + dp[i][0]
