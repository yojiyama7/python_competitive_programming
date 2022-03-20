from itertools import permutations as perm

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for l in perm(range(1, N)):
    l = [0] + list(l) + [0]
    cost = 0
    for j in range(N):
        cost += T[l[j]][l[j+1]]
    if cost == K:
        cnt += 1

print(cnt)
