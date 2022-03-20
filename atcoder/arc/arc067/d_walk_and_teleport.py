N, A, B = map(int, input().split())
X = list(map(int, input().split()))

cost = 0
pos = X[0]
for x in X[1:]:
    cost += min((x - pos)*A, B)
    pos = x

print(cost)
