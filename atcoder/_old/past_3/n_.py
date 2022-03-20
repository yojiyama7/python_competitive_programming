N, Q = map(int, input().split())
TXY = [list(map(int, input().split())) for _ in range(Q)]

l = list(range(1, N+1))
q = []
for t, x, y in TXY:
    if t == 2:
        l_, r_ = x, y
        for x2 in q:
            if x-1 <= l_ <= x+2:
                l_ = l_ + 2
            if x-1 <= r_ <= x+2:
                r_ = r_ - 2
            l[x2], l[x2+1] = l[x2+1], l[x2]
        print((x, l_), (r_, y))
        l[x:l_+1] = sorted(l[x:l_+1])
        l[r_:y+1] = sorted(l[r_:y+1])
        q = []
    else:
        q.append(x-1)
    # print(t, x, y, l)
print(*l)