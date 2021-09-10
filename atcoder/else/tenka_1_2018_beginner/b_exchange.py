A, B, K = map(int, input().split())

a, b = A, B
for i in range(K):
    if i%2 == 0:
        a >>= 1
        b += a
    else:
        b >>= 1
        a += b

print(a, b)
