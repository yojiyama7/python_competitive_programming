N = int(input())

primes = [2]
for i in range(3, N+1):
    if all(i % prime != 0 for prime in primes):
        primes.append(i)

count = 0
l = [0]*100
for i in range(N):
    for j in primes:
        if i % j == 0:
            l[j] += 1
    a = 1
    for j in l:
        a *= j+1
    if a == 75:
        count += 1

print(count)
