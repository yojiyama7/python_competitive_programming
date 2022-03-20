N = int(input())
A = list(map(int, input().split()))

if list(range(1, N+1)) == sorted(A):
    print("Yes")
else:
    print("No")
