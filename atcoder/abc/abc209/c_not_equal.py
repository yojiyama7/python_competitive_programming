MOD = 10**9+7

N = int(input())
C = list(map(int, input().split()))

C.sort()

ans = 1
for i, c in enumerate(C):
    ans *= max(0, c-i)
    ans %= MOD

print(ans)