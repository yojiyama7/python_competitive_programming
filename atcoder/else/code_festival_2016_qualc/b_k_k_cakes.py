K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = max(0, (A[-1]-1) - (sum(A[:-1])))

print(ans)