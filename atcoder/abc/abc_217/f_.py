# 区間dpってやつです

MOD = 998244353

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
# N = 200
# AB = []
# for i in range(1, 2*N+1):
#     for j in range(i+1, 2*N+1):
#         AB.append([i, j])
# M = len(AB)

g = [set() for i in range(2*N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)
def is_friend(a, b):
    return a in g[b]

dp = [[1 if l==r else 0 for r in range(2*N+1)] for l in range(2*N+1)]
for w in range(2, 2*N+1, 2):
    for l in range(2*N+1 - w):
        # O(N**2)
        r = l+w
        ans = 0
        if is_friend(l, r-1):
            ans += dp[l+1][r-1]
            ans %= MOD
        for k in range(l+2, r-1, 2):
            ans += dp[l][k] * dp[k][r] * 2
            ans %= MOD
        dp[l][r] = ans

print(dp[0][2*N])
# print(*dp)

################################

# import sys
# sys.setrecursionlimit(10**8)

# MOD = 998244353
# INF = 10**18

# N, M = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]
# # N = 50
# # AB = []
# # for i in range(1, 2*N+1):
# #     for j in range(i+1, 2*N+1):
# #         AB.append([i, j])
# # M = len(AB)

# g = [set() for i in range(2*N)]
# for a, b in AB:
#     a -= 1
#     b -= 1
#     g[a].add(b)
#     g[b].add(a)

# # cnt = 0
# memo = [[None for r in range(2*N+1)] for l in range(2*N+1)]
# def f(l, r):
#     if not(0 <= l <= 2*N and 0 <= r <= 2*N):
#         return 0
#     if l == r:
#         return 1
#     # global cnt
#     # cnt += 1
#     if memo[l][r] != None:
#         return memo[l][r]
#     ans = 0
#     for i in range(l, r-1):
#         for j in range(INF):
#             if 0 <= i-j < 2*N and i+1+j in g[i-j]:
#                 ans += f(l, i-j) * f(i+2+j, r)
#                 ans %= MOD
#             else:
#                 break
#     memo[l][r] = ans
#     return ans

# print(f(0, 2*N))
# # print(cnt)
