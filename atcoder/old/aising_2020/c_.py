N = int(input())

m = int(N**0.5) + 2
l = [0]*(N+1)

for x in range(1, m):
    for y in range(1, m):
        for z in range(1, m):
            r = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if r <= N:
                l[r] += 1
                # print(r, (x, y, z))

for i in range(1, N+1):
    print(l[i])