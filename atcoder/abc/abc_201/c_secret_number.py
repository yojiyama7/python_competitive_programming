S = input()

def is_valid(m):
	m = f"{m:0<4}"
	for i, s in enumerate(S):
		d = str(i)
		if s == 'o' and (not d in m):
			return False
		if s == 'x' and (d in m):
			return False
	return True

ans = 0
for i in range(10000):
	ans += is_valid(i)

print(ans)
