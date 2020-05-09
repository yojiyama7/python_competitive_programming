N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(N-1):
    a, b = A[i], A[i+1]
    if a < b:
        print("up", b-a)
    elif a == b:
        print("stay")
    else:
        print("down", a-b)