# 切り捨てに対する典型: 整数単位での関係性を探る
# 少数を作り出している部分を解決できるようにf(a) の a に演算をする

# 本問題に対する考察: f(a) -> f(a+100) の関係性
# f(a) = (100+t)*a//100
# //100 ということは
# f(a+100) = (100+t)*(a+100)//100
# f(a+100) = ((100+t)*a + (100+t)*100) // 100
# (100+t)*100 は 100の倍数なので 必ず 100 で割り切れる -> 切り捨ての外へ
# f(a+100) = (100+t)*a//100 + (100+t)
# f(a+100) = f(a) + (100+t)
# 規則性が見いだせる

T, N = map(int, input().split())

def intax(x):
    return (100+T)*x // 100

def is_ok(x):
    # print(intax(x), x)
    return (intax(x) - x) >= N

ok, ng = 10**12, 0
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(intax(ok)-1)
