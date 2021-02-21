N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cost = 0
resource = 0
for a, b in zip(A, B):
    if a < b:
        resource += (b - a) // 2
    elif a > b:
        cost += (a - b)

print("Yes" if cost <= resource else "No")