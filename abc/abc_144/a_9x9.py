A, B = list(map(int, input().split()))

print(A*B if all(1 <= x <= 9 for x in [A, B]) else -1)