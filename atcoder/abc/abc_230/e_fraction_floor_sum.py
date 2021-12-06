N = int(input())

def easy(x):
    ans = 0
    for i in range(1, x+1):
        ans += x//i
    return ans

def root_floor(x):
    ok, ng = 0, x
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if mid**2 <= x:
            ok = mid
        else:
            ng = mid
    return ok

def div_ceil(a, b):
    return -(-a//b)

ans = 0 
for i in range(1, root_floor(N)+1):
    l_mt = N//(i+1)
    r_le = div_ceil(N, i)
    cnt = r_le-l_mt - (l_mt < i <= r_le)
    score = i*cnt
    print(i, N//i, (l_mt+1, r_le+1), (l_mt < i <= r_le), score)
    ans += N//i + score

print(ans)
print(easy(N))