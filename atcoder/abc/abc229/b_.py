from itertools import zip_longest

A, B = input().split()

Arev, Brev = A[::-1], B[::-1]

for a, b in zip_longest(Arev, Brev, fillvalue='0'):
    a, b = int(a), int(b)
    if a + b > 9:
        print("Hard")
        exit()
print("Easy")
