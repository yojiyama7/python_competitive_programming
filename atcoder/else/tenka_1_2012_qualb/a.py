A, B, C = map(int, input().split())

for i in range(1, 128):
    if i%3 == A and i%5 == B and i%7 == C:
        print(i)