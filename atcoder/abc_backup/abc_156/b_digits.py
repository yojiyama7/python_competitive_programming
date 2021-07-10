N, K = list(map(int, input().split()))

c = 0
while N:
    c += 1
    N //= K

print(c)
