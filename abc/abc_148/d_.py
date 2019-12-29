N = int(input())
A = list(map(int, input().split()))

c = 0
for a in A:
    if a == c+1:
        c += 1

if c == 0:
    print(-1)
else:
    print(N-c)