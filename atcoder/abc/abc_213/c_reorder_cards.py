H, W, N = map(int, input().split())
AB = [map(int, input().split()) for _ in range(N)]
# AB = [
#     (1, 4),
#     (2, 3),
#     (4, 1),
#     (3, 2)
# ]
# H, W, N = 10**9, 10**9, len(AB)

A, B = zip(*AB)

A_dict = dict()
for i, a in enumerate(A):
    if a not in A_dict:
        A_dict[a] = []
    A_dict[a].append(i)
B_dict = dict()
for i, b in enumerate(B):
    if b not in B_dict:
        B_dict[b] = []
    B_dict[b].append(i)
A_l = sorted(A_dict.items())
B_l = sorted(B_dict.items())

# print(A_l, B_l)

ans = [[-1, -1] for _ in range(N)]
for i, (_, l) in enumerate(A_l):
    for l_j in l:
        ans[l_j][0] = i+1
for i, (_, l) in enumerate(B_l):
    for l_j in l:
        ans[l_j][1] = i+1

for yx in ans:
    print(*yx)
