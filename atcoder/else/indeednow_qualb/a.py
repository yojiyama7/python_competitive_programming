X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())

ans = abs(X1-X2) + abs(Y1-Y2) + 1
print(ans)