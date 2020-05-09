N = int(input())
A = list(map(int, input().split()))

print(*sorted(range(1, N+1), key=lambda x: A[x-1]))