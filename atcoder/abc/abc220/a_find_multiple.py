A, B, C = map(int, input().split())

for x in range(A, B+1):
    if x%C == 0:
        print(x)
        exit()
print(-1)
