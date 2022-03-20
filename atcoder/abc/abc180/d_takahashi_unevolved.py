X, Y, A, B = map(int, input().split())

st = X
ex = 0
while st*A <= st+B and st*A < Y:
    st *= A
    ex += 1

ex += ((Y-1)-st)//B

print(ex)
