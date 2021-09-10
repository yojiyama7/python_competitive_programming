A = int(input())

ok, ng = 0, 1000
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if mid**3 <= A:
        ok = mid
    else:
        ng = mid

if ok**3 == A:
    print("YES")
else:
    print("NO")
