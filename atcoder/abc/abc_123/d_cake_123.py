# 前提
# およそ O(10**8) まではOK

X, Y, Z, K = map(int, input().split(" "))
A, B, C = [list(map(int, input().split(" "))) for _ in range(3)]
# X, Y, Z, K = 1000, 1000, 1000, 3000
# A, B, C = [[i*j for j in range(1000)] for i in range(3)]

# l = []
# # 1000000000
# for a in A:
#     for b in B:
#         for c in C:
#             l.append(a+b+c)

# for l_i in sorted(l, reverse=True)[:K]:
#     print(l_i)

ab_cakes = []
# 1000000
for a in A:
    for b in B:
        ab_cakes.append(a+b)

# 1000000
ab_cakes = sorted(ab_cakes, reverse=True)[:K]

abc_cakes = []
# 3000000
for ab in ab_cakes:
    for c in C:
        abc_cakes.append(ab + c)

# 1000000
abc_cakes = sorted(abc_cakes, reverse=True)[:K]

# 3000
for abc in abc_cakes:
    print(abc)