N = int(input())
U = list(map(int, input().split(" ")))

b, *not_mins = sorted(U)
for u in not_mins:
    b = (b + u) / 2

print(b)
