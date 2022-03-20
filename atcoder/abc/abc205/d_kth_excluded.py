from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]

def solve(x):
    cnt = bisect_right(A, x)
    score = x - cnt
    return score

for k in K:
    ok = 10**19
    ng = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if solve(mid) >= k:
            ok = mid
        else:
            ng = mid
    print(ok)
