T = int(input())
NSK = [list(map(int, input().split())) for _ in range(T)]

def gcd(a, b):
    if a > b: a, b = b, a
    if a == 0: return b
    return gcd(a, b%a)

for N, S, K in NSK:
    if S%gcd(N, K) != 0:
        print(-1)
        continue
    pos = S
    cost = 0
    while pos:
        num = max((N - pos)//K, 1)
        pos = (pos + num*K) % N
        print(f"[num: {num}, (N, S, K): ({N}, {S}, {K}), pos: {pos}, cost: {cost}]")
        cost += num

