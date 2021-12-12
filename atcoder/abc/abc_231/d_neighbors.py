import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

deg = [0]*N
g = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    g[a].add(b)
    g[b].add(a)

stats = [0]*N
def check_has_cycle(i, before=None):
    if stats[i] == 1:
        return True
    stats[i] = 1
    for to in g[i]:
        if to == before:
            continue
        if check_has_cycle(to, i):
            return True
    stats[i] = 2
    return False
flag = 0
for i in range(N):
    if stats[i] == 0:
        if check_has_cycle(i):
            flag = 1

if all(d <= 2 for d in deg) and not flag:
    print("Yes")
else:
    print("No")
