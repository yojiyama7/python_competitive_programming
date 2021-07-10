N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

alcohol_x100 = 0
for i, (v, p) in enumerate(VP):
    alcohol_x100 += v*p
    if alcohol_x100 > X*100:
        print(i+1)
        exit()
print(-1)
