R, G, B, N = map(int, input().split())

cnt = 0
r = 0
while r*R <= N:
    g = 0
    while r*R + g*G <= N:
        if (N-r*R-g*G)%B == 0:
            cnt += 1
        g+=1
    r+=1

print(cnt)