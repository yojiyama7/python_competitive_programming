N, Q = map(int, input().split())
C = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]

for l, r in LR:
    

################################

# # そううまくはいかない
# # どこを、どうやって計算量を落とすか
# # https://hama-du-competitive.hatenablog.com/entry/2016/10/01/001418
# # "Range Distinct Query"
# from bisect import bisect_left

# N, Q = map(int, input().split())
# C = list(map(int, input().split()))
# LR = [list(map(int, input().split())) for _ in range(Q)]

# p = [[] for _ in range(N)]
# for i, c in enumerate(C):
#     c = c-1
#     p[c].append(i)

# q = [0]*N
# for l, r in LR:
#     m = 0
#     for p_i in p:
#         m += (bisect_left(p_i, r) - bisect_left(p_i, l-1)) >= 1
#     print(m)