# # TLE

# N = int(input())
# A = [[None]*(i+1) + list(map(int, input().split())) for i in range(2*N-1)]

# to_digit_idx = dict(((1<<i), i) for i in range(20))
# memo = [None for i in range(1<<2*N)]
# def solve(n, state):
#     # print((n, state))
#     if state == 0:
#         return [[]]
#     if memo[state] != None:
#         return memo[state]
#     ans = []
#     d = state&-state
#     state &= ~d
#     a = to_digit_idx[d]
#     # print([a])
#     for i in range(n):
#         if (state>>i)&1:
#             p = (a, i)
#             for li in solve(n, state & ~(1<<i)):
#                 ans.append([p] + li)
#     memo[state] = ans
#     return memo[state]

# ans = 0
# for p in solve(2*N, (1<<2*N)-1):
#     nums = [A[a][b] for a, b in p]
#     # print(nums)
#     score = 0
#     for n in nums:
#         score ^= n
#     ans = max(ans, score)

# print(ans)

################################

# N = int(input())
# A = [[None]*(i+1) + list(map(int, input().split())) for i in range(2*N-1)]

# # n%2 == 0
# def p1(n, zcnt=0):
#     if n == 0:
#         return ['']
#     ans_list = []
#     if n-zcnt > 0:
#         ans_list += ['('+s for s in p1(n-1, zcnt+1)]
#     if zcnt > 0:
#         ans_list += [')'+s for s in p1(n-1, zcnt-1)]
#     return ans_list

# print(len(p1(2*N)))

# max_score = 0
# for s in p1(2*N):
#     stack = []
#     score = 0
#     for j, c in enumerate(s):
#         if c == '(':
#             stack.append(j)
#         else:
#             a, b = stack.pop(), j
#             score ^= A[a][b]
#     max_score = max(score, max_score)

# print(max_score)

################################

# N = int(input())
# A = [[None]*i + list(map(int, input().split())) for i in range(2*N-1)]


# def patterns(l):
#     while 

# p = patterns(list(range(2*N)))
# print(p)