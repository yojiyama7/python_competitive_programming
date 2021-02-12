N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

ball = [1]*N
is_red = [0]*N
is_red[0] = 1

for x, y in XY:
    x, y = x-1, y-1
    if is_red[x]:
        is_red[y] = 1 
        if ball[x] == 1:
            is_red[x] = 0
    ball[x] -= 1
    ball[y] += 1
    # print(is_red, ball)

print(sum(is_red))
