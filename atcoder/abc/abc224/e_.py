INF = 10**18

H, W, N = map(int, input().split())
RCA = [list(map(int, input().split())) for _ in range(N)]

R, C, A = zip(*RCA)

rows = [-1 for _ in range(H)]
columns = [-1 for _ in range(W)]

l = dict()
for a in set(A):
    l[a] = []
for i, (r, c, a) in enumerate(RCA):
    r -= 1
    c -= 1
    l[a].append((r, c, i))

l = sorted(l.items(), reverse=True)

ans = [0 for _ in range(N)]
for a, rci_list in l:
    for r, c, i in rci_list:
        ans[i] = max(rows[r], columns[c]) + 1
    for r, c, i in rci_list:
        rows[r] = max(rows[r], ans[i])
        columns[c] = max(columns[c], ans[i])

print(*ans, sep='\n')
