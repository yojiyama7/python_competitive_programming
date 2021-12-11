N = int(input())

def easy(x):
    ans = 0
    for i in range(1, x+1):
        ans += x//i
    return ans

def solve(N):
    if N == 1:
        return 1
    def root_floor(x):
        ok, ng = 0, x
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if mid**2 <= x:
                ok = mid
            else:
                ng = mid
        return ok

    N_root_floor = root_floor(N)
    # print(f"root: {N_root_floor}")

    ans = 0 
    for i in range(1, N_root_floor+1):
        ans += N//i
    # print(ans)
    for i in range(1, N_root_floor+1):
        l_open = N//(i+1)
        r_close = N//i
        cnt = r_close-l_open - (l_open < i <= r_close)
        # print(i, (l_open, r_close), cnt)
        ans += i*cnt
    return ans

print(solve(N))
# for i in range(1, 10000):
#     if solve(i) == easy(i):
#         continue
#     print(i, solve(i), easy(i))
