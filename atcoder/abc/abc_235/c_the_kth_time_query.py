N, Q = map(int, input().split())
A = list(map(int, input().split()))
XK = [list(map(int, input().split())) for _ in range(Q)]

d = dict()
for i, a in enumerate(A):
    if a not in d:
        d[a] = []
    d[a].append(i+1)

for x, k in XK:
    k -= 1
    if x not in d:
        print(-1)
        continue
    if k < len(d[x]):
        print(d[x][k])
    else:
        print(-1)
