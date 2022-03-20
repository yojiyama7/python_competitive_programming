N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if P[i] == i+1:
        if i+1 != N:
            P[i], P[i+1] = P[i+1], P[i]
        cnt += 1

print(cnt)