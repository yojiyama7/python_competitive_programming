X, Y = map(int, input().split())

for a in range(0, X+1):
    b = X-a
    if a*2 + b*4 == Y:
        print("Yes")
        exit()
print("No")