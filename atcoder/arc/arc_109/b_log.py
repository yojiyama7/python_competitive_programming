N = int(input())

ok, ng = 0, 10**18
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if mid*(mid+1)//2 <= N+1:
        ok = mid
    else:
        ng = mid

print(N-ok+1)
