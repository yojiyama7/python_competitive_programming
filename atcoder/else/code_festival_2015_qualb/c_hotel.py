N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solve():
    if N < M:
        return "NO"
    A.sort(reverse=True)
    B.sort(reverse=True)
    if all (a >= b for a, b in zip(A, B)):
        return "YES"
    else:
        return "NO"

print(solve())
