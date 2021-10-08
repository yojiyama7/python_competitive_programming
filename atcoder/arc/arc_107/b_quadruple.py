N, K = map(int, input().split())

def f(x):
    l = max(1, x-N)
    r = min(N, x-1)
    return r-l+1

ans = 0
for ab in range(2, 2*N+1):
    cd = ab-K
    if not (2 <= cd <= 2*N):
        continue
    score = f(ab)*f(cd)
    ans += score
print(ans)