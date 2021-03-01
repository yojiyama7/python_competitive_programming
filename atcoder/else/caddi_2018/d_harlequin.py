N = int(input())
A = [int(input()) for _ in range(N)]

print("second" if all(a%2 == 0 for a in A) else "first")