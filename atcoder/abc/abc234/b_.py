N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x1, y1 in XY:
    for x2, y2 in XY:
        score = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
        ans = max(score, ans)

print(ans)