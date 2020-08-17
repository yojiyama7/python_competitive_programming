
################################

# # あとちょっとだったから、惜しかったと思います

# # WA, TLE

# # from itertools import accumulate as acc

# MOD = 10**9 + 7

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# A.sort()

# plus_list = []
# minus_list = []

# zero_count = 0
# for a in A:
#     # print(a)
#     if a > 0:
#         plus_list.append(a)
#     elif a < 0:
#         minus_list.append(a)
#     else:
#         zero_count += 1

# plus_list.sort()
# minus_list.sort()

# # def solve():
# #     # FIX: 大小を比べる方法 or 比べずに解決できる方法
# #     plus_list_reverse_acc = [1]
# #     for a in plus_list[::-1]:
# #         plus_list_reverse_acc.append(
# #             (plus_list_reverse_acc[-1] * a) % MOD
# #         )
# #     minus_list_acc = [1]
# #     for a in minus_list:
# #         minus_list_acc.append(
# #             (minus_list_acc[-1] * a) % MOD
# #         )
# #     # print(plus_list_reverse_acc, minus_list_acc)
# #     r = -(10**18)
# #     for minus_count in range(0, K+1, 2):
# #         if not (0 <= minus_count <= len(minus_list)):
# #             continue
# #         plus_count = K-minus_count
# #         if not (0 <= plus_count <= len(plus_list)):
# #             continue
# #         x = (minus_list_acc[minus_count] * plus_list_reverse_acc[plus_count]) % MOD
# #         r = max(r, x)
# #     return r

# def solve():
#     # print("A")
#     r = 1
#     minus_list_reverse = reversed(minus_list)
#     minus_pair_list = []
#     for i in range(0, len(minus_list), 2):
#         if i+1 < len(minus_list):
#             x = minus_list[i] * minus_list[i+1]
#             minus_pair_list.append(x)
#     minus_pair_list.reverse()
#     # print(plus_list, minus_pair_list)
#     q_num = 1
#     q_len = 0
#     while q_len < K:
#         if len(minus_pair_list) == 0 or ((len(plus_list) >= 2) and (plus_list[-2]*plus_list[-1] >= minus_pair_list[-1])) or q_len + 1 == K:
#             # print("{P")
#             q_num = (q_num * plus_list.pop()) % MOD
#             q_len += 1
#             # print(q_len)
#         else:
#             # print("P")
#             q_num = (q_num * minus_pair_list.pop())
#             q_len += 2
#     return q_num

# if plus_list and (not minus_list):
#     # print("plus")
#     if len(plus_list) < K:
#         r = 0
#     else:
#         r = 1
#         for a in plus_list[-K:]:
#             # print(r*a)
#             r = (r * a) % MOD
#         # print(A[-K:], r)
# elif (not plus_list) and minus_list:
#     # print("minus")
#     if K%2 == 1:
#         if zero_count:
#             r = 0
#         else:
#             r = 1
#             for a in minus_list[-K:]:
#                 r = (r * a) % MOD
#     else:
#         if len(minus_list) < K:
#             r = 0
#         else:
#             r = 1
#             for a in minus_list[:K]:
#                 r = (r * a) % MOD
# elif (not plus_list) and (not minus_list):
#     # print("zero")
#     r = 0
# else:
#     # print("plus minus zero")
#     # 2要素以上
#     if K == N:
#         r = (zero_count == 0)
#         for a in plus_list:
#             r = (r * a) % MOD
#         for a in minus_list:
#             r = (r * a) % MOD
#     else:
#         # K <= N-1:
#         # print(zero_count)
#         if zero_count:
#             # 3要素以上
#             if K > N-zero_count:
#                 r = 0
#             elif K == N-zero_count:
#                 if len(minus_list)%2 == 1:
#                     r = 0
#                 else:
#                     r = 1
#                     for a in plus_list:
#                         r = (r * a) % MOD
#                     for a in minus_list:
#                         r = (r * a) % MOD
#             else:
#                 r = solve()
#         else:
#             # 2要素以上 
#             r = solve()

# print(r)
