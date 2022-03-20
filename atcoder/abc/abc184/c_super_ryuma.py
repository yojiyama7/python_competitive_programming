# 最大3手

R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())

x, y = C2-C1, R2-R1

# print(x, y)

if x == y == 0:
    print(0)
elif (abs(x) + abs(y)) <= 3 or abs(x) - abs(y) == 0:
    print(1)
elif (abs(x) + abs(y)) <= 6 or abs(abs(x) - abs(y)) <= 3 or (x + y)%2 == 0:
    print(2)
else:
    print(3)
