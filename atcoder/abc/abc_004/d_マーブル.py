# 普通にTLE 1000**3 は無理でした
# 緑の置き場所を全探索
# 赤、青は基準点を中心にできるならして、
# 出来ない場合緑に接するようにするとコストが最小になる
# おそらく計算量1000でできる

# INF = float('inf')

# R, G, B = map(int, input().split(" "))

# # 閉区間　[a, b] (1 <= a, b)
# def sum_a_to_b(a, b):
#     if a > b:
#         return (0)
#     elif a == 1:
#         return b*(b+1)//2
#     else:
#         # (2 <= a, b)
#         return sum_a_to_b(1, b) - sum_a_to_b(1, a-1)

# def solve(std, left_pos, num):
#     if std < left_pos:
#         s = left_pos - std
#         e = s + num - 1
#         return sum_a_to_b(s, e)
#     elif left_pos <= std < left_pos+num:
#         l = std - left_pos
#         r = left_pos+num-1 - std
#         return sum_a_to_b(1, l) + sum_a_to_b(1, r)
#     elif left_pos+num <= std:
#         s = std - (left_pos+num-1)
#         e = s + num - 1
#         return sum_a_to_b(s, e)

# min_num = INF
# for r in range(-1010, 110):
#     score_r = solve(-100, r, R)
#     for g in range(r+R, 110):
#         score_g = solve(0, g, G)
#         for b in range(g+G, 110):
#             score_b = solve(100, b, B)
#             score = score_r + score_g + score_b
#             min_num = min(min_num, score)

################################

# R, G, B = map(int, input().split(" "))

# def sum_1_to_a(a):
#     return int((a+1)*(a/2))

# def solve_cost(num, first, std):
#     return sum_1_to_a(std) + sum_1_to_a(num-std-1)

# for g in range(G):
#     (R-1)//2