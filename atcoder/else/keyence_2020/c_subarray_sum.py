N, K, S = map(int, input().split())

l = [S]*K + [1 if S == 10**9 else 10**9]*(N-K)
print(*l)