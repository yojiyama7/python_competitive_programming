N = int(input())
X = list(map(int, input().split()))

print(sum(map(abs, X)))
print(sum(x**2 for x in X)**(1/2))
print(max(map(abs, X)))
