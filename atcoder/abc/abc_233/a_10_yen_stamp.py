X, Y = map(int, input().split())

cost = max(0, Y-X)
ans = -(-cost//10)
print(ans)