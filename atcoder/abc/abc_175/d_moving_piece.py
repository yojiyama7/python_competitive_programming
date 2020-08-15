from itertools import product
from itertools import accumulate as acc

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
# N, K = 5000, 10**9
# P = list(range(1, N+1))
# C = list(range(N, -1, -1))
# # print(len(P), len(C))

P = [p-1 for p in P]

visited = [0]*N
g = []
for i in range(N):
    if visited[i]:
        continue
    g.append([])
    # print(g)
    while visited[i] == 0:
        g[-1].append(i)
        visited[i] = 1
        i = P[i]
c = [[C[g_j] for g_j in g_i] for g_i in g]
c_acc = [[0]+list(acc(c_i*2)) for c_i in c]
c_sum = [sum(c_i) for c_i in c]
c_len = [len(c_i) for c_i in c]

max_num = -(10**18)
for i, g_i in enumerate(g):
    for j, start in enumerate(g_i):
        for k, end in enumerate(g_i*2):
            if not (j < k):
                continue
            cost = k-j
            score = c_acc[i][k+1] - c_acc[i][j+1]
            if c_sum[i] > 0:
                count = (K-cost)//c_len[i]
                cost += c_len[i]*count
                score += c_sum[i]*count
            if 1 <= cost <= K:
                max_num = max(max_num, score)
            # print((j, k), score)

print(max_num)