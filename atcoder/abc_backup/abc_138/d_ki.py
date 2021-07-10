N, Q = map(int, input().split(" "))
points = [0 for _ in range(N+1)]
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split(" "))
    g[a].append(b)
for _ in range(Q):
    p, x = map(int, input().split(" "))
    points[p] += x

q = [1]
while q:
    node = q.pop()
    for child in g[node]:
        points[child] += points[node]
        q.append(child)

print(*points[1:])

################################

# # AC

# from collections import deque

# N, Q = list(map(int, input().split(" ")))
# AB = [list(map(int, input().split(" "))) for _ in range(N-1)]
# PX = [list(map(int, input().split(" "))) for _ in range(Q)]

# points = [0 for _ in range(N+1)]
# g = [[] for _ in range(N+1)]
# for a, b in AB:
#     g[a].append(b)

# # print(g)

# for p, x in PX:
#     points[p] += x 

# q = deque([1])
# while q:
#     node = q.popleft()
#     for child in g[node]:
#         points[child] += points[node]
#         q.append(child)

# print(*points[1:])
