MOD = 998244353

ABC = list(map(int, input().split()))

def f(x):
    return (x*(x+1))//2

ans = 1
for x in ABC:
    ans *= f(x)
    ans %= MOD

print(ans)