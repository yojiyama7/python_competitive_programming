N = int(input())

r = N**2
l = 1
for i in range(N):
    l *= 2
    if l > r:
        break
if l > r:
    print("Yes")
else:
    print("No")