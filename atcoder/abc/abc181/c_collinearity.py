from fractions import Fraction

def is_line(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    if x2-x1 == 0 or x3-x2 == 0:
        return (x2-x1 == x3-x2 == 0)
    a = Fraction(y2-y1, x2-x1)
    b = Fraction(y3-y2, x3-x2)
    return (a == b)

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if is_line(XY[i], XY[j], XY[k]):
                print("Yes")
                exit()

print("No")