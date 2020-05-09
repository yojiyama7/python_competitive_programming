N, M = map(int, input().split())
A = list(map(int, input().split()))

x = N-(sum(A))

print(-1 if x < 0 else x)