INF = 10**18

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def make_frac(a, b):
    if b == 0:
        v = -INF if a < 0 else INF
        return (v, 1)
    posi_gcd = gcd(abs(a), abs(b))
    frac = (a//posi_gcd, b//posi_gcd)
    return frac

magics = set()
for i, (xi, yi) in enumerate(XY):
    for j, (xj, yj) in enumerate(XY):
        if i == j:
            continue
        w = xj-xi
        h = yj-yi
        magics.add(make_frac(h, w))
# print(magics)

ans = len(magics)
print(ans)