K = int(input())

b = 0
for i in range(1, 10**6+9):
    x = (b*10+7)%K
    if x == 0:
        print(i)
        exit()
    b = x

print(-1)