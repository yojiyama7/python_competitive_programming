# トポロジカルソートしたい

################################

# # TLE: 再帰部分が止まってる

# import sys
# sys.setrecursionlimit(2147483647)

# INF = float('inf')

# # N, M = map(int, input().split())
# # A = list(map(int, input().split()))
# # XY = [list(map(int, input().split())) for _ in range(M)]
# A = [i for i in range(2*10**5)]
# XY = [(i, i+1) for i in range(2*10**5-1)]
# N, M = len(A), len(XY)

# g = [set() for _ in range(N)]
# g_rev = [set() for _ in range(N)]
# for x, y in XY:
#     x, y = x-1, y-1
#     g[x].add(y)
#     g_rev[y].add(x)

# roots = [i for i, g_rev_i in enumerate(g_rev) if len(g_rev_i) == 0]
# # print(f"roots: {roots}")

# max_sell_price = [None for _ in range(N)]

# def solve_msp(x):
#     print(f"solve_msp({x})")
#     if max_sell_price[x] == None:
#         if len(g[x]) == 0:
#             max_sell_price[x] = -INF
#         else:
#             max_sell_price[x] = max(
#                 *(solve_msp(child) for child in g[x]),
#                 *(A[child] for child in g[x]),
#             )
#     return max_sell_price[x]

# for root in roots:
#     solve_msp(root)
# # print(f"max_sell_price: {max_sell_price}")

# max_num = -INF
# for i, a in enumerate(A):
#     if len(g[i]) == 0:
#         continue
#     score = -a + max_sell_price[i]
#     max_num = max(max_num, score)

# print(max_num)
