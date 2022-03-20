from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

counter = Counter(A)
counter_sum = sum(k*v for k, v in counter.items())

for b, c in BC:
    counter[c] += counter[b]
    counter_sum -= b * counter[b]
    counter_sum += c * counter[b]
    counter[b] = 0
    print(counter_sum)

