N = int(input())
A = list(map(int, input().split()))

f = lambda x: 0 if x%2 else f(x//2)+1

print(min(f(a) for a in A))