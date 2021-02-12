MOD = 10**9 + 7

N, K = map(int, input().split())
A = list(map(int, input().split()))

end_cnt = 0
for i in range(N):
    for j in range(i+1, N):
        end_cnt += (A[i] > A[j])
all_cnt = 0
for i in range(N):
    all_cnt += sum([a > A[i] for a in A])

ans = end_cnt*K
ans %= MOD
ans += all_cnt*((K)*(K-1)//2)
ans %= MOD

print(ans)
