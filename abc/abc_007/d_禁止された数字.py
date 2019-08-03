########################################

# # NO JUDGE

# A, B = map(int, input().split(" "))

# def count_ban(n):
#     print(f"start count_banned({n})")
#     if n == 0:
#         return 0
#     n_str = str(n)
#     n_len = len(n_str)
#     print(f"n_len: {n_len}")
#     not_ban = 0
#     for i, d in enumerate(map(int, n_str)):
#         remain_len = n_len-1-i
#         d_pattern = d - (d>4)
#         not_ban += d_pattern * (8**remain_len)
#         print(f"d_pattern: {d_pattern}, remain_len: {remain_len}")
#         print(f"not_ban: {not_ban}")
#         if d in [4, 9]:
#             break
#     ban = (n+1) - not_ban
#     return ban

# print(count_ban(A-1), count_ban(B))
# # print(count_ban(B)-count_ban(A-1))