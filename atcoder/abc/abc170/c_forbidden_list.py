X, N = map(int, input().split())
P = list(map(int, input().split()))

for i in range(101):
    for x in [X-i, X+i]:
        if x not in P:
            print(x)
            exit()
