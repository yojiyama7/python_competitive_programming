INF = 10**18

N, M = map(int, input().split())
A = list(map(int, input().split()))
# A = [2*3*5*7]*100000
# N, M = len(A), 100000

ans = [1]*100001

for a in A:
    for j in range(2, INF):
        if j*j > a:
            break
        if a%j == 0 and ans[j]:
            # print(j)
            for k in range(j, M+1, j):
                ans[k] = 0
        while a%j == 0:
            a //= j
    if a != 1 and ans[a]:
        for k in range(a, M+1, a):
            ans[k] = 0

p = [i for i in range(1, M+1) if ans[i]]
print(len(p))
print(*p, sep='\n')
