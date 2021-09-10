N = int(input())

v = [0]*31
for i in range(2, N+1):
    l = [0]*31
    for j in range(2, N+1):
        while i%j == 0:
            l[j] += 1
            i //= j
        if i == 1:
            break
    v = [max(v[i], l[i]) for i in range(31)]

# print(v)

ans = 1
for i, vi in enumerate(v):
    ans *= i**vi
ans += 1
print(ans)
