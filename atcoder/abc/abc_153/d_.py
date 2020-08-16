H = int(input())

def solve_cost(h):
    if h == 1:
        return 1
    return 1 + solve_cost(h//2)*2

print(solve_cost(H))