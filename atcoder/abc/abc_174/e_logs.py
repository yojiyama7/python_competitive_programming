BIG = 10**10

N, K = map(int, input().split())
A = list(map(int, input().split()))
# N, K = 2*10**5, 2*10**5
# A = [10**9]*N

def solve(x):
    m = 0
    for a in A:
        m += -(-(a//x))
    # print(x, m)
    return m > K

A = [a*BIG for a in A]

# c = 0
ok, ng = 0, max(A)
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    # print(mid)
    if solve(mid):
        ok = mid
    else:
        ng = mid
    # c += 1

# print(c)

print(-(-ok//BIG))