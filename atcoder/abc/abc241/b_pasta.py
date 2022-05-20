from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

remain = Counter(A)

for b in B:
    if b not in remain or remain[b] == 0:
        print("No")
        exit()
    remain[b] -= 1

print("Yes")