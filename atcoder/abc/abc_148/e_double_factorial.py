N = int(input())

def solve(n):
    if n%2 == 1:
        return 0
    sum_num = 0
    for i in range(1000):
        m = n//2 // (5**(i+1))
        if m == 0:
            break
        sum_num += m
        # print(m)
    return sum_num

print(solve(N))