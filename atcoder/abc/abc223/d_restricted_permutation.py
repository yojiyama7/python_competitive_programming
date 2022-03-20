from heapq import *
import sys
sys.setrecursionlimit(10**8)

class HeapMin:
    def __init__(self, l=[], key=lambda x:x):
        self.key = key
        self.l = [(self.key(l_i), l_i) for l_i in l]
        heapify(self.l)

    def push(self, v):
        heappush(self.l, (self.key(v), v))

    def pop(self):
        _, r = heappop(self.l)
        return r

    def __bool__(self):
        return len(self.l) > 0

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

indeg = [0]*N
g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    if b not in g[a]:
        g[a].add(b)
        indeg[b] += 1
# print(indeg)

visited = [0]*N
def is_loop(i):
    if visited[i] == 1:
        return True
    if visited[i] == 2:
        return False
    visited[i] = 1
    for to in g[i]:
        if is_loop(to):
            return True
    visited[i] = 2
    return False

for i in range(N):
    if is_loop(i):
        print(-1)
        exit()

ans_0idx = []
q = HeapMin([i for i in range(N) if indeg[i] == 0])
while q:
    t = q.pop()
    ans_0idx.append(t)
    for to in g[t]:
        indeg[to] -= 1
        if indeg[to] == 0:
            q.push(to)
ans = [x+1 for x in ans_0idx]
print(*ans)

################################

# # しゅうちゅうできん

# from heapq import *

# class HeapMin:
#     def __init__(self, l=[], key=lambda x:x):
#         self.key = key
#         self.l = [(self.key(l_i), l_i) for l_i in l]
#         heapify(self.l)

#     def push(self, v):
#         heappush(self.l, (self.key(v), v))

#     def pop(self):
#         _, r = heappop(self.l)
#         return r

#     def __bool__(self):
#         return len(self.l) > 0

# N, M = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]

# indeg = [0]*N
# g = [set() for _ in range(N)]
# for a, b in AB:
#     a -= 1
#     b -= 1
#     if b not in g[a]:
#         g[a].add(b)
#         indeg[b] += 1
# # print(indeg)

# q = HeapMin()
# for i in range(N):
#     if indeg[i] == 0:
#         q.push(i)
# if not q:
#     print(-1)
#     exit()

# visited = [0]*N
# ans = []
# while q:
#     print(q.l)
#     print(visited)
#     print(ans)
#     t = q.pop()
#     if visited[t] == 1:
#         print(-1)
#         exit()
#     if visited[t] == 2:
#         continue
#     visited[i] = 1
#     ans.append(t)
#     for to in g[t]:
#         indeg[to] -= 1
#         if indeg[to] == 0:
#             q.push(to)
#     visited[t] = 2

# if len(ans) == N:
#     print(*ans)
# else:
#     print(-1)

# # visited = [0]*N
# # def is_loop(i):
# #     if visited[i] == 1:
# #         return True
# #     if visited[i] == 2:
# #         return False
# #     visited[i] = 1
# #     for to in g[i]:
# #         if is_loop(to):
# #             return True
# #     visited[i] = 2
# #     return False

# # if is_loop(0):
# #     print(-1)
# #     exit()

