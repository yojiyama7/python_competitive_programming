N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

max_score = 0
for i in range(1<<K):
    l = [0]*N
    for j, cd in enumerate(CD):
        l[cd[(i>>j)&1]-1] = 1
    score = sum(l[a-1] and l[b-1] for a, b in AB)
    max_score = max(score, max_score)

print(max_score)
