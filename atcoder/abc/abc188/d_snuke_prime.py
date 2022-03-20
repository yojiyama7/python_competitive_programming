N, C = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

d = {10**9+1: 0}
for a, b, c in ABC:
    a, b, c = a-1, b, c
    if a not in d:
        d[a] = 0
    if b not in d:
        d[b] = 0
    d[a] += c
    d[b] -= c

l = sorted(d.items())
sum_num = 0
cost = 0
b_k = 0
for k, v in l:
    sum_num += min(cost, C) * (k - b_k)
    cost += v
    b_k = k

print(sum_num)