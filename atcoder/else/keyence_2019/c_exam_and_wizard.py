N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()

cnt = 0
l = []
cost = 0
for i in range(N):
    if A[i] >= B[i]:
        l.append(A[i] - B[i])
    else:
        cost += B[i] - A[i]
        cnt += 1

l.sort(reverse=True)
for l_i in l:
    if cost <= 0:
        break
    cnt += 1
    cost -= l_i

print(cnt)
