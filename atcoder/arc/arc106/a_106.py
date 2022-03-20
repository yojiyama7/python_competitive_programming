INF = 10**18

N = int(input())

for a in range(1, INF):
    if 3**a > N:
        break
    for b in range(1, INF):
        x = 3**a + 5**b
        if x > N:
            break
        if x == N:
            print(a, b)
            exit()
print(-1)
