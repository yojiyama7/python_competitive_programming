L = int(input())

result = 1
for i in range(L-11, L):
    result *= i

print(result//39916800)