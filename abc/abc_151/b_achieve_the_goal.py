N, K, M = map(int, input().split())
A = list(map(int, input().split()))

p = max(0, M*N-sum(A))
if p <= K:
    print(p)
else:
    print(-1)