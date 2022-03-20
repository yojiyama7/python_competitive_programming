R, X, Y = map(int, input().split())

d = (X**2 + Y**2) ** (1/2)

if d < R:
	print(2)
elif d == R:
	print(1)
else:
	print(-int(-d//R))
