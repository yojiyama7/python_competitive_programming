N, M, K = map(int, input().split())

for i in range(N+1):
    for j in range(M+1):
        # print(i, j)
        if i*M + j*N - 2*i*j == K:
            print("Yes")
            exit()
print("No")
