N, K = map(int, input().split())
DA = [(int(input()), list(map(int, input().split()))) for _ in range(K)]

l = [0]*N
for d, a in DA:
    for ai in a:
        ai = ai-1
        l[ai] += 1

print(l.count(0))