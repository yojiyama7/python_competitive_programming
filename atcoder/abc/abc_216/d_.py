N, M = map(int, input().split())
KA = [(int(input()), list(map(int, input().split()))) for _ in range(M)]

# N = 2*10**5
# M = 2*10**5
# KA = [[1, [i//2+1]] for i in range(M)]
# N = 2*10**5
# M = 2
# KA = [[N//2, [j+1 for j in range(N//2)]] for _ in range(M)]

K, A = zip(*KA)

top = [0]*N
idx = [[] for _ in range(N)]

q = list(range(M))
while q:
    t = q.pop()
    # print(t, "---")
    if not A[t]:
        continue
    col = A[t][-1] -1
    idx[col].append(t)
    if len(idx[col]) == 2:
        x, y = idx[col]
        A[x].pop()
        A[y].pop()
        q.append(x)
        q.append(y)

if any(A):
    print("No")
else:
    print("Yes")
