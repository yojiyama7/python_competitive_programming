N = int(input())
TXY = [list(map(int, input().split())) for _ in range(N)]

bt, bx, by = 0, 0, 0
for t, x, y in TXY:
    time = t-bt
    size = abs(x-bx) + abs(y-by)
    if size > time or size%2 != time%2:
        print("No")
        exit()
    bt, bx, by = t, x, y
print("Yes")