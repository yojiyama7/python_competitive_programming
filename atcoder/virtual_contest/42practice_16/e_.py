from itertools import combinations as combi

INF = float('inf')

N, *ABC = map(int, input().split())
L = [int(input()) for _ in range(N)]

min_num = INF
for i in range(4**N):
    abc_ = [[], [], [], []]
    for j in range(N):
        abc_[i//(4**j) % 4].append(L[j])
    cost = 0
    if not all(abc_[:3]):
        continue
    for lis, ans in zip(abc_[:3], ABC):
        cost += 10*(len(lis)-1) + abs(sum(lis)-ans)
    # print(abc_, cost)
    min_num = min(cost, min_num)

print(min_num)
