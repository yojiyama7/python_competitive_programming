N = int(input())
A = list(map(int, input().split()))

print(3**N - 2**(sum(a%2 == 0 for a in A)))