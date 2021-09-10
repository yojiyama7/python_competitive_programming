N = int(input())

table = [1]*N

for i in range(2, N):
    if table[i] == 0:
        continue
    for j in range(2*i, N, i):
        table[j] = 0

ans = sum(table[2:])
print(ans)