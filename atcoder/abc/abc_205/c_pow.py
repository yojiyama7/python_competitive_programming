A, B, C = map(int, input().split())

x, y = A, B
if x < 0 and C%2 == 0:
    x *= -1
if y < 0 and C%2 == 0:
    y *= -1
# print(x, y)
if x == y:
    print('=')
elif x < y:
    print('<')
else:
    print('>')
