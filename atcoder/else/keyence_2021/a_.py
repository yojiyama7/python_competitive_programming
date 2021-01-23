N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_max = [0]*N
for i, a in enumerate(A):
    if i == 0:
        A_max[i] = a
    else:
        A_max[i] = max(A_max[i-1], a)

dp = [0 for _ in range(N)]
dp[0] = A[0]*B[0]
for i in range(1, N):
    # print("i: {i}")
    dp[i] = max(
        dp[i-1],
        A_max[i] * B[i]
    )

print(*dp, sep='\n')