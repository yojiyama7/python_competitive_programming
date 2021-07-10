N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

min_num = 10**18
for i in range(1<<N):
    cost = 0
    l = [0]*M
    for j in range(N):
        if (i>>j)&1:
            c, *a = CA[j]
            cost += c
            for k, ak in enumerate(a):
                l[k] += ak
    if all(lj >= X for lj in l):
        min_num = min(min_num, cost)
    # print(l)

print(-1 if min_num == 10**18 else min_num)