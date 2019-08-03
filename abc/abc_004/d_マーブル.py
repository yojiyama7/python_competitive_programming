R, G, B = map(int, input().split(" "))

def sum_1_to_a(a):
    return int((a+1)*(a/2))

def solve_cost(num, first, std):
    return sum_1_to_a(std) + sum_1_to_a(num-std-1)

for g in range(G):
    (R-1)//2