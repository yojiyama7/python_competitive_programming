H, W = map(int, input().split())

if H == 1:
    print(W)
elif W == 1:
    print(H)
else:
    print(-(-W//2) * -(-H//2))
