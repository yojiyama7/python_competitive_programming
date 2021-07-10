# 中心選びが悪そう？

# 視点をかえて、各点を中心にして一定の半径で円を書いて交点をとり、そのうちある点が全ての円に入っていればその半径以下
# ということを利用して、二分探索

# 二分探索の視点は良かった。
# 円の中に内包される点は交点を利用するのがよさげ


# N**3 * log(1500000000)
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
# N = 50
# XY = [(0, i) for i in range(N)]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = (abs(x1-x2)**2 + abs(y1-y2)**2) ** (1/2)
    return d
def mid_p(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = (x1+x2)/2, (y1+y2)/2
    return m
def is_in_circle(a, center, radius):
    r = all(distance(a_i, center) <= radius for a_i in a)
    return r

min_num = 10**18
for i, p1 in enumerate(XY):
    for j, p2 in enumerate(XY):
        center = mid_p(p1, p2)
        ok = 1500
        ng = 0
        while ok-ng > 10**-7:
            mid = (ok+ng) / 2
            if is_in_circle(XY, center, mid):
                ok = mid
            else:
                ng = mid
        min_num = min(min_num, ok)

print(min_num)