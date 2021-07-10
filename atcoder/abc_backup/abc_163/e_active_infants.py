N = int(input())
A = list(map(int, input().split()))

l = [(i, a) for i, a in enumerate(A)]

score = 0
for _ in range(N):
    for i in range(N-1):
        a, b = l[i], l[i+1]
        a_np = abs(a[0]-i)*a[1]
        b_np = abs(b[0]-(i+1))*b[1]
        np = a_np + b_np
        a_sp = abs(a[0]-(i+1))*a[1]
        b_sp = abs(b[0]-i)*b[1]
        sp = a_sp + b_sp
        diff = sp - np
        if diff >= 0:
            l[i], l[i+1] = l[i+1], l[i]
            score += diff

print(score)