N, M = list(map(int, input().split()))
SC = [list(map(int, input().split())) for _ in range(M)]

for i in range(1000):
    t = str(i)
    if len(t) == N and all([(len(t) > s-1) and (int(t[s-1]) == c) for s, c in SC]):
        print(i)
        exit()
print(-1)
