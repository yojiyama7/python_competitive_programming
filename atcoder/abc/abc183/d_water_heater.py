from itertools import accumulate as acc

N, W = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(N)]

l = [0]*200001
for s, t, p in STP:
    l[s] += p
    l[t] -= p

print("Yes" if all(x <= W for x in acc(l)) else "No")
