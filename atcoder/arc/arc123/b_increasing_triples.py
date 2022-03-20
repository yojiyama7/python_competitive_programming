N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0
b, c = 0, 0
for a in range(N):
    while b < N and B[b] <= A[a]:
        b += 1
    if not b < N:
        break
    while c < N and C[c] <= B[b]:
        c += 1
    if not c < N:
        break
    if A[a] < B[b] < C[c]:
        ans += 1
        a += 1
        b += 1
        c += 1
print(ans)