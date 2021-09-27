N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

xyi = [(x, y, i) for i, (x, y) in enumerate(XY)]

l = []
xyi.sort()
l += xyi[:2] + xyi[-2:]
xyi.sort(key=lambda x: x[1])
l += xyi[:2] + xyi[-2:]

l = list(set(l))
ans = []
for i in range(len(l)):
    x1, y1, _ = l[i]
    for j in range(i+1, len(l)):
        x2, y2, _ = l[j]
        p = max(abs(x1-x2), abs(y1-y2))
        ans.append(p)

ans.sort(reverse=True)

print(ans[1])