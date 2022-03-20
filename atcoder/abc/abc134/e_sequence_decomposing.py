INF = 10**18

N = int(input())
A = [int(input()) for _ in range(N)]

def bisect_right_rev(l, a):
    ok = 0
    ng = len(l)+1
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if l[mid-1] >= a:
            ok = mid
        else:
            ng = mid
    return ok

l = []
for a in A:
    idx = bisect_right_rev(l, a)
    if idx == len(l):
        l.append(a)
    else:
        l[idx] = a

# print(A, l)
ans = len(l)
print(ans)