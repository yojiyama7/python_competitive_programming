N = 10000000

ans = 0
for i in range(1, N):
    ans += N//i

print(N, ans, ans/N)