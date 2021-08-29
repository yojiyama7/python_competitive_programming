################################

# INF = 10**18

# N = int(input())
# S = list(map(int, input()))
# T = list(map(int, input()))

# # 00 -> 00
# # 01 -> 01, 10
# # 10 -> 10
# # 11 -> 11, 00
# # つまり, 1は2個セットで消せるかつ, 左側に一つ移動できる
# # 1の時 発動するかしないかを選ぶ -> 必然と決まる？ そうでもないな

# memo = [None]*(N+1)
# def solve(i):
#     print(i)
#     if i == 0:
#         return 0
#     if memo[i] != None:
#         return memo[i]
#     memo[i] = INF
#     if S[i-1] == T[i-1]:
#         memo[i] = min(memo[i], solve(i-1))
#     if i == 1:
#         return memo[i]
#     a, b = 2*S[i-2]+S[i-1], 2*T[i-2]+T[i-1]
#     if a == 1 and b == 2:
#         memo[i] = min(memo[i], solve(i-2)+1)
#     elif a == 3 and b == 0:
#         memo[i] = min(memo[i], solve(i-2)+1)
#     return memo[i]

# ans = solve(N)
# print(memo)
# print(ans)

################################

# N = int(input())
# S = list(map(int, input()))
# T = list(map(int, input()))

# a, b = sum(S), sum(T)
# if a < b or a%2 != b%2:
#     print(-1)
#     exit()

# s, t = S[:], T[:]
# cnt = 0
# for i in reversed(range(1, N)):
#     if s[i] == t[i] == 1:
#         continue
#     if s[i] == 0:
#         print(-1)
#         exit()
#     # s[i] == 1 and t[i] == 0
#     s[i] = 0
#     s[i-1] = (s[i-1]+1)%2
#     cnt += 1

# print(cnt, s, t)

