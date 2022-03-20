N, K = map(int, input().split())
A = list(map(int, input().split()))

def f(x):
    return ((x+1)*x)//2

all_ans = sum(map(f, A))
if sum(A) <= K:
    print(all_ans)
    exit()

def is_ok(x):
    cost = sum(max(0, a-x) for a in A)
    # print(x, cost)
    return cost <= K

ok, ng = all_ans, 0
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

# print(ok, ng)

ans = sum(f(a)-f(ok) for a in A if a > ok)
cost = sum(max(0, a-ok) for a in A)
ans += (K-cost)*ok

print(ans)
