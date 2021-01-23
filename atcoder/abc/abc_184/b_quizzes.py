N, X = map(int, input().split())
S = input()

p = X
for s in S:
    if s == 'o':
        p += 1
    elif s == 'x' and p > 0:
        p -= 1

print(p)
