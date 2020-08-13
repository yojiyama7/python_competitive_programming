N, M = map(int, input().split())
A = list(map(int, input().split()))

childs = [[] for _ in range(N)]

l = [0 for _ in range(N)]
for i, a in enumerate(A):
    ng, ok = -1, N
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if l[mid] < a:
            ok = mid
        else:
            ng = mid
    index = ok
    if index < N:
        l[index] = a
        childs[index].append(i)
    # print(l)

sushi = [-1]*M
for i, child in enumerate(childs):
    for eated in child:
        sushi[eated] = i+1

for sushi_i in sushi:
    print(sushi_i)