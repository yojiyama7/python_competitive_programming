# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1167&lang=jp

# INF = 10**20

# A = []
# N = 0
# while True:
#     tmp = int(input())
#     if tmp:
#         A.append(tmp)
#         N += 1
#     else:
#         break

# dp = [INF for _ in range(10**6+1)]
# dp[0] = 0
# dp_odd = [INF for _ in range(10**6+1)]
# dp_odd[0] = 0

# for j in range(1, INF):
#     x = j*(j+1)*(j+2)//6
#     for i in range(10**6+1):
#         if i-x < 0:
#             break
#         if dp[i] > dp[i-x] + 1:
#             dp[i] = dp[i-x] + 1
#         if x%2 and dp_odd[i] > dp_odd[i-x] + 1:
#             dp_odd[i] = dp_odd[i-x] + 1
#     if x%2:
#         for i in range(10**6+1):
#             if i-x < 0:
#                 break
#             if dp_odd[i] > dp_odd[i-x] + 1:
#                 dp_odd[i] = dp_odd[i-x] + 1

# for a in A:
#     print(dp[a], dp_odd[a])

################################

# いや通るんかい
# ACかい
# まあ工夫ということでいいよもう

from itertools import product

INF = 10**20

A = []
N = 0
while True:
    tmp = int(input())
    if tmp:
        A.append(tmp)
        N += 1
    else:
        break

# print(A)

l = [0]
for i in range(1, INF):
    x = l[-1] + (i*(i+1)//2)
    if x > 10**6:
        break
    l.append(x)

l1 = set(l)
l2 = {a+b for a, b in product(l, repeat=2)}
l3 = {a+b+c for a, b, c in product(l, repeat=3)}

ans1 = [None]*N

for i, a in enumerate(A):
    if a in l1:
        ans1[i] = 1
    elif a in l2:
        ans1[i] = 2
    elif a in l3:
        ans1[i] = 3
    else:
        for l2_i in l2:
            if a-l2_i in l2:
                ans1[i] = 4
    if ans1[i] == None:
        ans1[i] = 5

# print(len(l))
# print(l)
p = [l_i for l_i in l if l_i%2]
# print(len(p))
# print(p)

dp = [INF]*(10**6+1)
dp[0] = 0

for i in range(1, 10**6+1):
    for x in p:
        if i-x < 0:
            break
        dp[i] = min(
            dp[i-x] + 1,
            dp[i],
        )

for i, a in enumerate(A):
    print(ans1[i], dp[a])
