A, B = map(int, input().split())

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    return a*b//gcd(a, b)

ans = lcm(A, B)
if ans > 10**18:
    print("Large")
else:
    print(ans)
