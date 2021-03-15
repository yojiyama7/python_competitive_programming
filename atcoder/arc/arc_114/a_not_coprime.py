INF = float('inf')

N = int(input())
X = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

is_prime = [1]*51
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, 51):
    if is_prime[i] == 0:
        continue
    for j in range(2*i, 51, i):
        is_prime[j] = 0

primes = [i for i in range(2, 51) if is_prime[i]]

min_num = INF
for i in range(1<<len(primes)):
    m = 1
    for j in range(len(primes)):
        if (i>>j)&1:
            m *= primes[j]
    if all(gcd(x, m) != 1 for x in X):
        min_num = min(min_num, m)

print(min_num)

################################

# 貪欲的には出来ない

# # WA

# N = int(input())
# X = list(map(int, input().split()))

# primes = [0]*51
# for x in X:
#     s = set()
#     # print(x)
#     for j in range(2, 51):
#         if x%j == 0:
#             s.add(j)
#         while x%j == 0:
#             x //= j
#     # print(s)
#     if all(primes[s_i] == 0 for s_i in s):
#         primes[min(s)] = 1

# ans = 1
# for i, p in enumerate(primes):
#     if p:
#         ans *= i

# print(ans)
