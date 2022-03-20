N = int(input())
A = [int(input()) for _ in range(N)]

def solve():
    if A[0] != 0:
        return -1
    cost = A[N-1]
    for i in reversed(range(N-1)):
        d = A[i+1]-A[i]
        if d > 1:
            return -1
        elif d == 1:
            pass
        else:
            cost += A[i]
    # print(i, cost)
    return cost

print(solve())