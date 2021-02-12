from collections import Counter

MOD = 998244353

N = int(input())
D = list(map(int, input().split()))

def solve():
    if D[0] != 0:
        return (0)
    if any(d == 0 for d in D[1:]):
        return (0)
    max_depth = max(D)
    D_counter = Counter(D)
    # print(D_counter)
    sum_num = 1
    for i in range(max_depth):
        sum_num *= pow(D_counter[i], D_counter[i+1], MOD)
        sum_num %= MOD
    return (sum_num)

print(solve())
