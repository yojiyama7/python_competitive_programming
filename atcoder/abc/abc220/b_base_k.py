K = int(input())
A, B = input().split()

x = 0
for i, a in enumerate(A[::-1]):
    x += int(a) * K**i
y = 0
for i, b in enumerate(B[::-1]):
    y += int(b) * K**i

print(x*y)
