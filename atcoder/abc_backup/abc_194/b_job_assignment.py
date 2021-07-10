N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A, B = zip(*AB)

ans = min(map(sum, AB))
for i, a in enumerate(A):
    for j, b in enumerate(B):
        if i == j:
            continue
        ans = min(ans, max(a, b))
print(ans)