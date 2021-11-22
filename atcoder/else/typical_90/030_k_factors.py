N, K = map(int, input().split())

table = [0]*(N+1)
for i in range(2, N+1):
    if table[i]:
        continue
    for j in range(i, N+1, i):
        table[j] += 1

# print(table)

ans = sum(table[i] >= K for i in range(N+1))
print(ans)
