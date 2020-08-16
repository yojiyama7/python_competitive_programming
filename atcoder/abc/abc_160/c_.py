K, N = map(int, input().split())
A = list(map(int, input().split()))

max_num = A[0] + (K - A[-1])
for i in range(N-1):
    max_num = max(max_num, A[i+1] - A[i])

print(K-max_num)