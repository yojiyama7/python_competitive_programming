import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].add(b)
    g[b].add(a)

cnt = 0
visited = [0]*N

def solve(i):
    visited[i] = 1
    for to in g[i]:
        if visited[to]:
            continue
        solve(to)

for i in range(N):
    if visited[i]:
        continue
    solve(i)
    cnt += 1

print(cnt-1)