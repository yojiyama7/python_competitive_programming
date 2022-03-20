N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(x):
    score = sum(min(a, x) for a in A)
    return score >= K*x

ok, ng = 0, 10**18+1
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        # print('ok:', mid)
        ok = mid
    else:
        # print('ng:', mid)
        ng = mid

print(ok)
