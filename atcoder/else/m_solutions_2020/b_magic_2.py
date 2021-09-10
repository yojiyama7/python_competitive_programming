A, B, C = map(int, input().split())
K = int(input())

cost = 0

while A >= B:
    B *= 2
    cost += 1

while B >= C:
    C *= 2
    cost += 1

if cost <= K:
    print("Yes")
else:
    print("No")