N = int(input())
XY = [tuple(map(int, input().split())) for i in range(N)]

XY_set = set(XY)

ans = 0
for x1, y1 in XY:
    for x2, y2 in XY:
        if not (x1 < x2 and y1 < y2):
            continue
        if (x2, y1) in XY_set and (x1, y2) in XY_set:
            ans += 1

print(ans)