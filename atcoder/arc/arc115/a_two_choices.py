N, M = map(int, input().split())
S = [input() for _ in range(N)]

even, odd = 0, 0
for s in S:
    if sum(map(int, s)) % 2:
        odd += 1
    else:
        even += 1

print(odd*even)
