N = int(input())
A = list(map(int, input().split()))

ans = sum(a-10 for a in A if a >= 10)
print(ans)
