AX, AY, BX, BY = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

def is_cross_line_straight_segment(l1, ls2):
    p1, p2 = l1
    p3, p4 = ls2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    # (y1-y2)*(x1-X) + (x1-x2)*(Y-y1) : 正負で直線にたいしてどちら側かわかる
    x, y = x3, y3
    r3 = (y1-y2)*(x1-x) + (x1-x2)*(y-y1)
    x, y = x4, y4
    r4 = (y1-y2)*(x1-x) + (x1-x2)*(y-y1)
    ans = r3*r4 < 0
    return ans

def is_cross_line_segments(ls1, ls2):
    if not is_cross_line_straight_segment(ls1, ls2):
        return False
    if not is_cross_line_straight_segment(ls2, ls1):
        return False
    return True

ls1 = ((AX, AY), (BX, BY))
cnt = 0
for i in range(N):
    ls2 = (XY[i], XY[(i+1)%N])
    # print(ls1, ls2)
    if is_cross_line_segments(ls1, ls2):
        cnt += 1

# print(cnt)
ans = cnt//2+1
print(ans)
