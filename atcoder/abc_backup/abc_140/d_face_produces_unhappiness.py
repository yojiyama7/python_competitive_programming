N, K = map(int, input().split())
S = input()

def g(t):
    l = []
    b = "x"
    c = 0
    for i, t_i in enumerate(t):
        if b != t_i:
            l.append(c)
            c = 0
        c += 1
        b = t_i
    l.append(c)
    return l[1:]

l = g(S)
len_l = len(l)
score = sum(l)-len_l

score += min(len_l//2, K)*2 - (len_l%2==0 and len_l//2 <= K)

print(score)
################################ 

# # AC

# from itertools import groupby, accumulate

# N, K = map(int, input().split())
# S = input()

# l = [len(list(g)) for k, g in groupby(S)]
# # print(l)
# m = min(len(l)//2, K)
# # print(m)
# a = [0]*(N+1)
# x = 0
# for l_i in l[:m]:
#     x += l_i
#     a[x] += 1
# x = N
# for l_i in l[-m:][::-1]:
#     x -= l_i
#     if a[x] == 0:
#         a[x] -= 1

# # print(list(accumulate(a))[:-1])

# s_list = list(S)
# for i, b in enumerate(list(accumulate(a))[:-1]):
#     if b%2:
#         s_list[i] = "R" if S[i] == "L" else "L"

# # print(s_list)

# count = 0
# for i, s_i in enumerate(s_list):
#     if s_i == "L":
#         if i == 0:
#             continue
#         count += s_list[i-1] == "L"
#     else:
#         if i == N-1:
#             continue
#         count += s_list[i+1] == "R"

# print(count)
