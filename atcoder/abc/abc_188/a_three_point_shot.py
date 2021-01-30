XY = list(map(int, input().split()))

print("Yes" if min(XY) + 3 > max(XY) else "No")
