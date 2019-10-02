N = int(input())
A = list(map(int, input().split()))

A.sort()

min_num = 10**18
for i in range(N):
    x, y = A[i::N]
    min_num = min(min_num, abs(x-y))

print(min_num)
