INF = float('inf')

N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]

XL.sort(key=lambda v: v[0]+v[1])

cnt = 0
right = -INF
for x, l in XL:
    # print((x, l), right)
    if right <= (x - l):
        # print("a")
        cnt += 1
        right = x + l

print(cnt)
