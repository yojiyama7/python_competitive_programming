N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

c = A[:]
# print(c)
point = 0
for i in range(N):
    p = min(c[i], B[i])
    c[i] -= p
    point += p
    p = min(c[i+1], B[i]-p)
    c[i+1] -= p
    point += p

print(point)