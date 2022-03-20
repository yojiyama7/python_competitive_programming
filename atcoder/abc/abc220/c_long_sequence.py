N = int(input())
A = list(map(int, input().split()))
X = int(input())

A_sum = sum(A)

ans = (X//A_sum)*N

p = A_sum*(X//A_sum)
for i in range(N):
    p += A[i]
    ans += 1
    if p > X:
        break

print(ans)
