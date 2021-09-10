from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

correct = Counter("indeednow")
for s in S:
    if Counter(s) == correct:
        print("YES")
    else:
        print("NO")