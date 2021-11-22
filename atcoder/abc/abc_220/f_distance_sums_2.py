from collections import deque
import sys
sys.setrecursionlimit(10**8)

INF = 10**18

N = int(input())
UV = [list(map(int, input().split())) for _ in range(N-1)]

g = [set() for _ in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    g[u].add(v)
    g[v].add(u)

depth = [INF]*N
depth[0] = 0
q = deque([0])
while q:
    t = q.popleft()

    for to in g[t]:
        if depth[to] < depth[t] + 1:
            continue
        depth[to] = depth[t] + 1
        q.append(to)

# print(depth)

subcnt = [None]*N
def solve_subcnt(i):
    if subcnt[i] != None:
        return subcnt[i]
    ans = 1
    # print(i, g[i])
    for to in g[i]:
        if depth[to] > depth[i]:
            ans += solve_subcnt(to)
    subcnt[i] = ans
    return subcnt[i]
solve_subcnt(0)
# print(subcnt)

ans_list = [None]*N
ans_list[0] = sum(depth)
s = [0]
while s:
    t = s.pop()

    for to in g[t]:
        if depth[to] > depth[t]:
            ans_list[to] = ans_list[t] + N - 2*subcnt[to]
            s.append(to)

print(*ans_list, sep='\n')
