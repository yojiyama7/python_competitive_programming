from math import factorial

N, D = map(int, input().split(" "))
X, Y = map(int, input().split(" "))

if not (X%D == 0 and Y%D == 0):
    print(0)
    exit()
x, y = abs(X//D), abs(Y//D)
if N%2 != (x+y)%2:
    print(0)
    exit()

