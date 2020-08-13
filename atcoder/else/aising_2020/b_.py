N = int(input())
A = list(map(int, input().split()))

print(sum([i%2 == 0 and a%2 == 1 for i, a in enumerate(A)]))