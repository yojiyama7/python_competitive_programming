INF = 10**18

N, D = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]

lr_list = [(l-1, r) for l, r in LR]
lr_list.sort(lambda lr: lr[1])

ans = 0
broked = -INF
for l, r in lr_list:
    if not(r <= broked or broked+D <= l):
        continue
    broked = r-1
    ans += 1

print(ans)
