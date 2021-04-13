V, E = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(E)]

g = [set() for _ in range(V)]
in_cnt = [0]*V
for s, t in ST:
    g[s].add(t)
    in_cnt[t] += 1

res = []
q = [i for i, m in enumerate(in_cnt) if m == 0]
while q:
    t = q.pop()
    res.append(t)

    for c in g[t]:
        in_cnt[c] -= 1
        if in_cnt[c] == 0:
            q.append(c)

print(*res, sep="\n")
