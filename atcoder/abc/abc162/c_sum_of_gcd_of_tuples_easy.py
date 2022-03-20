from itertools import product

K = int(input())

def gcd_ab(a, b):
    # print(a, b)
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd_ab(b, a%b)

def gcd(*args):
    r = args[0]
    for arg in args[1:]:
        r = gcd_ab(r, arg)
    return r

sum_num = 0
for a, b, c in product(range(1, K+1), repeat=3):
    sum_num += gcd(a, b, c)

print(sum_num)