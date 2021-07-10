from collections import deque
 
MOD = 10**9+7
 
N = int(input())
A, B = map(int, input().split())
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]
 
# N = 12
# A, B = 1, 12
# XY = [
#     (1, 1),
#     (1, 3),
#     (1, 4),
#     (1, 11),
#     (2, 3),
#     (3, 5),
#     (4, 5),
#     (11, 10),
#     (5, 7),
#     (5, 6),
#     (10, 6),
#     (10, 7),
#     (6, 8),
#     (6, 9),
#     (7, 8),
#     (7, 9),
#     (8, 12),
#     (9, 12)
# ]
# M = len(XY)
 
start, goal = A-1, B-1
 
g1 = [set() for _ in range(N)]
for x, y in XY:
    x, y = x-1, y-1
    g1[x].add(y)
    g1[y].add(x)
 
count = [0]*N
count[start] = 1
dist = [10**18]*N
dist[start] = 0
q = deque([start])
while q:
    t = q.popleft()
    t_dist = dist[t]
    t_count = count[t]
 
    for c in g1[t]:
        if dist[c] > t_dist + 1:   
            dist[c] = t_dist + 1
            q.append(c)
        if dist[c] == t_dist + 1:
            count[c] = (count[c] + t_count) % MOD
 
# print(dist)
# print(count)
print(count[goal])


################################

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