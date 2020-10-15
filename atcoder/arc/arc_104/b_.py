from itertools import accumulate as acc

N, S = input().split()
N = int(N)

atcg_l = [[0]*N for _ in range(4)]

for i, s in enumerate(S):
    t = "ATCG".find(s)
    atcg_l[t][i] = 1

atcg_acc = [[0]+list(acc(x_l)) for x_l in atcg_l]
# [print(x_acc) for x_acc in atcg_acc]

cnt = 0
for i in range(N):
    for j in range(N+1):
        if i >= j:
            continue
        a, t, c, g = [x_acc[j] - x_acc[i] for x_acc in atcg_acc]
        # print(a, t, c, g, a == t, c == g)
        if a == t and c == g:
            cnt += 1

print(cnt)
