A, B = map(int, input().split())

def f(a, x):
    return a//x

ans = 1
for i in range(2, B+1):
    if f(B, i) - f(A-1, i) >= 2:
        ans = i

print(ans)