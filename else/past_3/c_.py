A, R, N = map(int, input().split())

def solve():
    if R == 1:
        return A
    m = A
    for i in range(N-1):
        m *= R
        if m > 10**9:
            return "large"
    return m

print(solve())
