N, A, X, Y = map(int, input().split())

print(X*min(A, N) + Y*max(N-A, 0))