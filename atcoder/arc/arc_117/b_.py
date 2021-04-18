MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 1
b = 0
for a in A:
    ans *= (a - b + 1)
    ans %= MOD
    b = a

print(ans)