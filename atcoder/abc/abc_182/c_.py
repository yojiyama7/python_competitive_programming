INF = float('inf')

N = input()
K = len(N)

min_num = INF
for i in range(1<<K):
    cnt = 0
    mod_num = 0
    for j in range(K):
        if (i>>j)&1:
            mod_num = (mod_num + int(N[j])) % 3
        else:
            cnt += 1
    if mod_num == 0 and cnt < K:
        min_num = min(min_num, cnt)

print(-1 if min_num == INF else min_num)
