K, N, M = map(int, input().split())
A = list(map(int, input().split()))

# abs(Bi*N - Ai*M)

def is_ok(x):
    # |Ai*M - Bi*N| <= x
    # -x <= Ai*M - Bi*N <= x
    # x >= Bi*N - Ai*M >= -x
    # x + Ai*M >= Bi*N >= -x + Ai*M
    # (x + Ai*M)/N >= Bi >= (-x + Ai*M)/N
    # (-x + Ai*M)/N <= Bi <= (x + Ai*M)/N
    # Bi は整数なので
    # ceil((-x + Ai*M)/N) <= Bi <= floor((x + Ai*M)/N)
    min_sum = 0
    max_sum = 0
    for a in A:
        min_b = max(-(-(-x + a*M)//N), 0)
        max_b = (x + a*M)//N
        min_sum += min_b
        max_sum += max_b
    return (min_sum <= M <= max_sum)

def solve(x):
    min_sum = 0
    max_sum = 0
    ans = []
    for a in A:
        min_b = max(-(-(-x + a*M)//N), 0)
        max_b = (x + a*M)//N
        ans.append(min_b)
        min_sum += min_b
        max_sum += max_b
    current_sum = min_sum
    for i, a in enumerate(A):
        max_b = (x + a*M)//N
        diff = M - current_sum
        p = min(diff, max_b-ans[i])
        ans[i] += p
        current_sum += p
    return ans

ok, ng = 10**15, -1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(*solve(ok))
