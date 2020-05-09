N, X, Y = list(map(int, input().split()))

X, Y = X-1, Y-1

def solve_shortest(a, b):
    if a > b:
        a, b = b, a
    l = [
        b - a,
        abs(X - a) + 1 + abs(b - Y)
    ]
    # print(min(l), (a, b), X, Y, l)
    return min(l)

counts = [0]*N
for i in range(N):
    for j in range(N):
        if i < j:
            counts[solve_shortest(i, j)] += 1

for i in range(1, N):
    print(counts[i])