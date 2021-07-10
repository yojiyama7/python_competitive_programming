A, B, C, K = map(int, input().split())

a = min(A, K)
K -= a
b = min(B, K)
K -= b
c = min(C, K)

print(a-c)