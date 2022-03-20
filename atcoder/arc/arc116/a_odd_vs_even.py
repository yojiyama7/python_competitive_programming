T = int(input())

for _ in range(T):
    N = int(input())

    cnt = 0
    while N%2 == 0:
        N //= 2
        cnt += 1
        if cnt == 2:
            break
    if cnt == 1:
        print("Same")
    elif cnt == 0:
        print("Odd")
    else:
        print("Even")