N = int(input())

s = set()
for i in range(2, N+1):
	if i**2 > N:
		break
	for j in range(2, 50):
		if i**j > N:
			break
		# print(f"{i}**{j} == {i**j}")
		s.add(i**j)

print(N-len(s))
