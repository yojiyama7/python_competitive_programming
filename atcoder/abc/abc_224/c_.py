from itertools import combinations as combi

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for (p, q), (a, b), (x, y) in combi(XY, 3):
    # print(p, q, a, b, x, y)
    a -= p
    b -= q
    x -= p
    y -= q
    if x*b != a*y:
        ans += 1

print(ans)
