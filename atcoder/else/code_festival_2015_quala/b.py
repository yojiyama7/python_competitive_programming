N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans *= 2
    ans += a

print(ans)