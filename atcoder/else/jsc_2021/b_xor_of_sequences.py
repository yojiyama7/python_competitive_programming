N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = set(A), set(B)
ans = sorted((a | b) - (a & b))
print(*ans)
