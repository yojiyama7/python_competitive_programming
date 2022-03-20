

################################

# from collections import deque

# WIN, LOSE, DRAW = range(3)
# P = 52**3

# N = int(input())
# S = [input() for _ in range(N)]

# def to_num_inner(c):
#     if ord('a') <= ord(c) <= ord('z'):
#         return ord(c) - ord('a')
#     else:
#         return ord(c) - ord('A') + 26

# def to_num(t):
#     x = 0
#     for i, t_i in enumerate(t):
#         x += 52**i * to_num_inner(t_i)
#     return x

# g = [set() for _ in range(P)]
# # g における 自分の子供のうち まだ score が定まっていないもの の個数
# cnt = [0]*P
# g_rev = [set() for _ in range(P)]
# for s in S:
#     f, t = to_num(s[:3]), to_num(s[-3:])
#     g[f].add(t)
#     cnt[f] += 1
#     g_rev[t].add(f)

# score = [DRAW]*P
# q = deque()
# for i in range(P):
#     if cnt[i] == 0:
#         q.append(i)

# # 結果が決定した場所 + そこと連結な場所 について答えを考える必要がある (qに入る必要がある)
# while q:
#     t = q.popleft()

#     l = [0, 0, 0]
#     for to in g[t]:
#         l[score[to]] += 1
#     win, lose, draw = l
#     if lose:
#         score[t] = WIN
#     elif lose+draw == 0:
#         score[t] = LOSE
#     else:
#         score[t] = DRAW
#     for to in g_rev[t]:
#         cnt[to] -= 1
#         if cnt[to] == 0:
#             q.append(to)

# for s in S:
#     ans = score[to_num(s[-3:])]
#     if ans == WIN:
#         print("Aoki")
#     elif ans == LOSE:
#         print("Takahashi")
#     else:
#         print("Draw")

################################

# # import sys
# # sys.setrecursionlimit(10**8)
# from collections import deque

# WIN, LOSE, DRAW = range(3)

# N = int(input())
# S = [input() for _ in range(N)]

# def to_num_inner(c):
#     if ord('a') <= ord(c) <= ord('z'):
#         return ord(c) - ord('a')
#     else:
#         return ord(c) - ord('A') + 26

# def to_num(t):
#     x = 0
#     for i, t_i in enumerate(t):
#         x += 52**i * to_num_inner(t_i)
#     return x

# g = [set() for _ in range(52**3)]
# g_rev = [set() for _ in range(52**3)]
# for s in S:
#     f, e = to_num(s[:3]), to_num(s[-3:])
#     g[f].add(e)
#     g_rev[e].add(f)

# ans = [-1]*(52**3)
# q = deque([0])
# for s in S:
#     x = to_num(s[-3:])
#     if len(g[x]) == 0:
#         ans[x] = LOSE
#         q.append(x)

# # for s in S:
# #     x = to_num(s[-3:])
# #     if ans[x] == WIN:
# #         print("Aoki")
# #     elif ans[x] == LOSE:
# #         print("Takahashi")
# #     elif ans[x] == -1 or ans[x] == DRAW:
# #         print("Draw")
# #     else:
# #         print("?")

# while q:
#     t = q.popleft()
#     print("#", t)
#     for to in g[t]:
#         if ans[to] != -1:
#             continue
#         if len(g_rev[to]) == 0:
#             ans[to] = LOSE
#         elif all(b == WIN for b in g_rev[t]):
#             ans[to] = LOSE
#         elif LOSE in g_rev[t]:
#             ans[to] = WIN
#         else:
#             ans[to] = DRAW
#         q.append(to)

# for s in S:
#     x = to_num(s[-3:])
#     if ans[x] == WIN:
#         print("Aoki")
#     elif ans[x] == LOSE:
#         print("Takahashi")
#     elif ans[x] == -1 or ans[x] == DRAW:
#         print("Draw")
#     else:
#         print("?")

# # result = [-1]*(52**3)
# # def solve(i):
# #     if result[i] != -1:
# #         return result[i]
# #     around = [False]*3
# #     for to in g[i]:
# #         around[solve(to)] = True
# #     win, lose, draw = around
# #     if lose:
# #         result[i] = 0
# #     elif lose+draw == 0 or win+lose+draw == 0:
# #         result[i] = 1
# #     else:
# #         result[i] = 2
# #     return result[i]

# # for s in S:
# #     ans = solve(to_num(s[-3:]))
# #     # print(ans)
# #     print(["Aoki", "Takahashi", "Draw"][ans])
