import sys

sys.setrecursionlimit(10**8)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
for i in range(N):
    g[i].sort()

# print(g)

visited = [0]*N
ans = []
def dfs(idx):
    visited[idx] = 1
    ans.append(idx+1)
    for to in g[idx]:
        if visited[to]:
            continue
        dfs(to)
        if ans[-1] != idx+1:
            ans.append(idx+1)

dfs(0)
print(*ans)
