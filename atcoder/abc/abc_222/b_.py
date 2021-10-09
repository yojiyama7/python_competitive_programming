N, P = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(a<P for a in A)

print(ans)