N, Q = map(int, input().split())
QUERY = [list(map(int, input().split())) for _ in range(Q)]

front = [-1]*N
back = [-1]*N
for t, *args in QUERY:
    if t == 1:
        x, y = args
        x -= 1
        y -= 1
        back[x] = y
        front[y] = x
    elif t == 2:
        x, y = args
        x -= 1
        y -= 1
        back[x] = -1
        front[y] = -1
    else:
        x, = args
        x -= 1
        while front[x] != -1:
            x = front[x]
        ans = []
        while x != -1:
            ans.append(x+1)
            x = back[x]
        print(len(ans), *ans)
    # print(front, back)
