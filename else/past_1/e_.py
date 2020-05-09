N, Q = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(Q)]

l = [0 for _ in range(N)]

for s in S:
    x, *ab = s
    # print(x, ab)
    if x == 1:
        a, b = ab[0]-1, ab[1]-1
        # a -> b
        l[a] |= 1<<b
    elif x == 2:
        a = ab[0]-1
        for i, p in enumerate(l):
            if (p>>a)&1:
                l[a] |= 1<<i
    else:
        a = ab[0]-1
        # print(bin(l[a])[2:])
        l_a_old = l[a]
        for i in range(N):
            if (l_a_old>>i)&1:
                # print(i)
                l[a] |= l[i]
    # for p in l:
    #     t = "".join(["NY"[(p>>i)&1] for i in range(N)])
    #     print(t)


for i in range(N):
    l[i] = ~(~l[i] | (1<<i))
            
for p in l:
    t = "".join(["NY"[(p>>i)&1] for i in range(N)])
    print(t)
        