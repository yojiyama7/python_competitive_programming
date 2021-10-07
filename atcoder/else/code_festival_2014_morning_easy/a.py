N = int(input())
A = list(map(int, input().split()))

ans = sum(A[i+1] - A[i] for i in range(N-1))/(N-1)

print(ans)
