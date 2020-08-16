import sys
sys.setrecursionlimit(10**8)

A, B = map(int, input().split())

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    return (a*b) // gcd(a, b)

print(lcm(A, B))