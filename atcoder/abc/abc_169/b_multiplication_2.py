N = int(input())
A = list(map(int, input().split()))

def solve():
    if 0 in A:
        return 0
    m = 1
    for a in A:
        m *= a
        if m > 10**18:
            return -1
    return m

print(solve())