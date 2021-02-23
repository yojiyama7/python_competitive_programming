# 今まで使った文字の中で**最大**の文字+1まで使える

from itertools import zip_longest

N = int(input())

# def convert_to_normal(s):
#     is_visited = [0]*26
#     converted = ["_"]*26
#     x = 0
#     for s_i in s:
#         num = ord(s_i) - ord('a')
#         if is_visited[num]:
#             continue
#         is_visited[num] = 1
#         converted[num] = chr(ord('a') + x)
#         x += 1
#     t = "".join(converted[ord(s_i) - ord('a')] for s_i in s)
#     return t

t = [[0]]
for i in range(1, N):
    q = []
    for t_j in t:
        for k in range(max(t_j) + 2):
            q.append(t_j + [k])
    # print(q)
    t = q

# if len(t) != len(set(map(tuple, t))):
#     print("length is different")

# chars = "abcdefghij"[:N]
# def all_pattern(i):
#     if i == 0:
#         return [""]
#     l = []
#     for p in all_pattern(i-1):
#         for c in chars:
#             l.append(p + c)
#     return (l)

l = ["".join([chr(ord('a') + t_ij) for t_ij in t_i]) for t_i in t]
[print(l_i) for l_i in l]

# a = [p for p in sorted(all_pattern(N)) if p == convert_to_normal(p)]
# [print(a_i) for a_i in a]

# if l != a:
#     print("DIFF")
#     for l_i, a_i in zip_longest(l, a, fillvalue="_"*N):
#         print(l_i, a_i, (l_i != a_i)*"DIFF")

################################

# t = "abcdefghijk"[:N]
# def solve(idx):
#     if idx == 0:
#         return [""]
#     l = []
#     for s in solve(idx-1):
#         for t_i in t:
#             l.append(s + t_i)
#     return (l)

# print(solve(N))
# # for s in solve(N):
