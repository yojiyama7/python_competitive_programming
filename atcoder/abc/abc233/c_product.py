from itertools import product

N, X = map(int, input().split())
LA = [list(map(int, input().split())) for _ in range(N)]

L, A = zip(*[(l, a) for l, *a in LA])

ans = 0
for idxs in product(*map(range, L)):
    score = 1
    for a, idx in zip(A, idxs):
        score *= a[idx]
    if score == X:
        ans += 1

print(ans)
