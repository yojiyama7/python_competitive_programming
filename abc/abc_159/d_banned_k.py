from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A_counter = Counter(A)
full_score = 0
for k, v in A_counter.items():
    full_score += v*(v-1)//2

for a in A:
    print(full_score - (A_counter[a]-1))