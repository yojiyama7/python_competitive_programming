N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

g = [set() for i in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    g[a].add(b)
    g[b].add(a)

c = 0
for i in range(N):
    if all(H[c]<H[i] for c in g[i]):
        c += 1

print(c)