from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A_counter = Counter(A)
# print(A_counter)
print(len(A_counter) - sum((v-1)%2 for v in A_counter.values())%2)