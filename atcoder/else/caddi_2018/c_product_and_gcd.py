from collections import Counter

N, P = map(int, input().split())

primes = Counter()
i = 2
num = P
while i*i <= P:
    while num%i == 0:
        primes[i] += 1
        num //= i
    i+=1
if num != 1:
    primes[num] += 1

# print(primes)

ans = 1 
for k, v in primes.items():
    if v//N:
        ans *= k**(v//N)
print(ans)
