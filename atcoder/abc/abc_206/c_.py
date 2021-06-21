from collections import Counter

N = int(input())
A = list(map(int, input().split()))

score = N*(N-1)//2

for v in Counter(A).values():
    score -= v*(v-1)//2

print(score)
