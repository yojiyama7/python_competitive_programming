N = int(input())
A = list(map(int, input().split()))

A.sort()

def solve(x):
    size = A[x]
    for i, a in enumerate(A):
        if i == x:
            continue
        if a <= size*2:
            size += a
        else:
            return (False)
    return (True)

ng = -1
ok = N-1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid

print(N-ok)