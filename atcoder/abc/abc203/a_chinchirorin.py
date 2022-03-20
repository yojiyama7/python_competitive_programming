A, B, C = list(map(int, input().split()))

if A == B:
	print(C)
elif B == C:
	print(A)
elif C == A:
	print(B)
else:
	print(0)