INF = 10**18

A, B, C = map(int, input().split())

cycle = None
for i in range(1, INF):
    if A%10 == pow(A%10, i+1, 10):
        cycle = i
        break

b_c = (pow(B, C, cycle)-1)%cycle + 1
ans = pow(A%10, b_c, 10)
print(ans)
