X = int(input())

def gcd(a, b):
    # print(a, b)
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

print(lcm(360, X)//X)
