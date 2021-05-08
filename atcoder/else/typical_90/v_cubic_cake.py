A, B, C = map(int, input().split())

def gcd(a, b):
	return (b if a == 0 else gcd(b%a, a))

x = gcd(gcd(A, B), C)

ans = A//x + B//x + C//x - 3

print(ans)