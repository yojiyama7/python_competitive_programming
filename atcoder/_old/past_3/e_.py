N, M, Q = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(M)]
C = list(map(int, input().split()))
S = [input().split() for _ in range(Q)]

g = [set() for _ in range(N)]
for u, v in UV:
    u, v = u-1, v-1
    g[u].add(v)
    g[v].add(u)

colors = C

for s in S:
    if s[0] == "1":
        x = int(s[1])-1
        print(colors[x])
        for child in g[x]:
            colors[child] = colors[x]
    elif s[0] == "2":
        x, y = int(s[1])-1, int(s[2])
        print(colors[x])
        colors[x] = y