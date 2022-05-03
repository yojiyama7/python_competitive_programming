N = int(input())
A = [[None]*(i+1) + list(map(int, input().split())) for i in range(2*N-1)]



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