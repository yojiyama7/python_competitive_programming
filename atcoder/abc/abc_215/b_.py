N = int(input())

ok, ng = 0, 60
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if 2**mid <= N:
        ok = mid
    else:
        ng = mid

print(ok)