from collections import deque

N = int(input())
A, B = map(int, input().split())
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for x, y in XY:
    x, y = x-1, y-1
    g[x].add(y)
    g[y].add(x)

counts = [0]*N
counts[A-1] = 10**18
r = [10**18]*N
r[A-1] = 0
q = deque([A-1])
while q:
    tn = q.popleft()
    tr = r[tn]

    for cn in g[tn]:
        if cn == tn:
            continue
        if r[cn] <= tr:
            continue
        if counts == 0:
            q.append(cn)
        counts[cn] += 1

print(r)




##################################################

# これDPとかなの？ まあWAくらってるけどさ

################################
#-------------------------------
################################

# N = int(input())
# A, B = map(int, input().split(" "))
# M = int(input())
# XY = [list(map(int, input().split(" "))) for _ in range(M)]

# routes = [set() for _ in range((N+1))]
# for x, y in XY:
#     routes[x].add(y)
#     routes[y].add(x)

# visited = set()
# # visited.add(A)
# p = [0]*(N+1)
# p[A] = 1

# now_q = {A}
# while now_q:
#     next_q = set()
#     for this_n in now_q:
#         visited.add(this_n)

#         for n in routes[this_n]-visited:
#             p[n] = (p[n]+p[this_n]) % (10**9+7)
#             next_q.add(n)
#     if B in next_q:
#         break
#     now_q = next_q

# print(p[B])

# # print(0)

################################

# from collections import deque

# N = int(input())
# A, B = map(int, input().split(" "))
# M = int(input())
# XY = [list(map(int, input().split(" "))) for _ in range(M)]

# routes = [set() for _ in range((N+1))]
# for x, y in XY:
#     routes[x].add(y)
#     routes[y].add(x)

# visited = set()
# # visited.add(A)
# p = [0]*(N+1)
# p[A] = 1

# can_append = True
# q = deque([A])
# while q:
#     this_n = q.popleft()
#     print(this_n, routes[this_n])
#     # if this_n == B:
#     #     flag = True

#     flag = False
#     for n in routes[this_n]-visited:
#         visited.add(n)
#         if n == B:
#             flag = True
#             print(q)
#         # print(n, this_n, p[n], p[this_n])
#         p[n] = (p[n]+p[this_n]) % (10**9+7)
#         if can_append:
#             q.append(n)
#     print(p, flag)
#     if flag:
#         can_append = False

# print(p[B])