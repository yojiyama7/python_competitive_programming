# ABC 002 D - 派閥
# https://atcoder.jp/contests/abc002/tasks/abc002_4

N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

d = [0 for _ in range(N)]
for i in range(N):
    d[i] |= 1<<i
for x, y in XY:
    d[x-1] |= 1<<(y-1)
    d[y-1] |= 1<<(x-1)

max_count = 0
for i in range(1<<N):
    x = i
    count = 0
    for j in range(N):
        if (i>>j)%2:
            x &= d[j]
            count += 1
    if x == i:
        max_count = max(max_count, count)

print(max_count)