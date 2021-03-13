from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A_counter = Counter(A)
sum_num = 0
for k1, v1 in A_counter.items():
    for k2, v2 in A_counter.items():
        if k1 == k2:
            continue
        m = v1*v2
        sum_num += ((k1 - k2) ** 2) * m

sum_num //= 2

print(sum_num)
