N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# print([i for i in range(N-1) if A[i]+1 == A[i+1]])
# print(C)
print(sum(B)+sum([C[A[i]-1] for i in range(N-1) if A[i]+1 == A[i+1]]))