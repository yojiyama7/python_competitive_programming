N = int(input())
A = list(map(int, input().split(" ")))

print(sum(sorted(A, reverse=True)[::2]))