N = int(input())

m = 0
for i in range(1, N+1):
    m += i
    if m >= N:
        print(i)
        exit()
