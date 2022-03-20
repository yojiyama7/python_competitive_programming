N, X = map(int, input().split())
A = list(map(int, input().split()))

known = [0]*N
p = X-1
while known[p] == 0:
    known[p] = 1
    p = A[p]-1

print(sum(known))