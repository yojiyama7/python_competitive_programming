X, K, D = map(int, input().split())

X = abs(X)

if X//D <= K:
    K -= X//D
    X %= D

    X -= D*(K%2)

    print(abs(X))
else:
    print(X - D*K)