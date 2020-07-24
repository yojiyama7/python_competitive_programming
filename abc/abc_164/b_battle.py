A, B, C, D = map(int, input().split())

i = 0
while A > 0 and C > 0:
    if i%2 == 0:
        C -= B
    else:
        A -= D
    i += 1

print("Yes" if A > 0 else "No")