N = int(input())
A = list(map(int, input().split()))

l = [(a, i) for i, a in enumerate(A)]
l.sort()

print(l[-2][1] + 1)
