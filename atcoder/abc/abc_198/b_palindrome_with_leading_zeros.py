N = input()

while N and N[-1] == '0':
	N = N[:-1]

if N == N[::-1]:
	print("Yes")
else:
	print("No")