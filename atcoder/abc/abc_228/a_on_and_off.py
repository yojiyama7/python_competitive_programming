S, T, X = map(int, input().split())

m = S
while True:
    if m == T:
        break
    if m == X:
        print("Yes")
        exit()
    m = (m+1)%24

print("No")
