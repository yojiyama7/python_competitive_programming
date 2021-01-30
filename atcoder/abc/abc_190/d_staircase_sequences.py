N = int(input())

cnt = 0
i = 1
while ((i+1)*i)//2 <= N:
    if i%2 == 1 and N%i == 0:
        # print(N, i)
        cnt += 2
    if i%2 == 0 and (N-(((1+i)*i)//2))%i == 0:
        cnt += 2
    i+=1

print(cnt)
