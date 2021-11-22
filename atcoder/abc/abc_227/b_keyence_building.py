N = int(input())
S = list(map(int, input().split()))

valid = set()
for a in range(1, 1001):
    for b in range(1, 1001):
        valid.add(4*a*b + 3*a + 3*b)

ans = 0
for s in S:
    if s not in valid:
        ans += 1

print(ans)
