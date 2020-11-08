import math

def gcd(a, b, c):
    return math.gcd(math.gcd(a, b), c)

K = int(input())

sum_num = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            sum_num += gcd(a, b, c)

print(sum_num)
