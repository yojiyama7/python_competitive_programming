M, D = map(int, input().split())

ans = 0
for i in range(1, M+1):
    for j in range(1, D+1):
        a, b = j//10, j%10
        if a >= 2 and b >= 2 and a*b == i:
            ans += 1

print(ans)