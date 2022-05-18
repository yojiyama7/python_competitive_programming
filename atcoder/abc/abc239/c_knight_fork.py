X1, Y1, X2, Y2 = map(int, input().split())

dpos = [
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
    (2, 1),
    (-2, 1),
    (2, -1),
    (-2, -1),
]

a = {(X1+dx, Y1+dy) for dx, dy in dpos}
b = {(X2+dx, Y2+dy) for dx, dy in dpos}

if a&b:
    print("Yes")
else:
    print("No")