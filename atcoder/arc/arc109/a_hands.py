A, B, X, Y = map(int, input().split())

# A, B: l, r

up = min(Y, 2*X)
lr = X
l_up = X

if A > B:
    print(l_up + up*(A-B-1))
else:
    print(lr + up*(B-A))
