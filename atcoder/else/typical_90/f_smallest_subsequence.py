from collections import Counter, deque

N, K = map(int, input().split())
S = input()
# N, K = 100000, 50000
# S = "z"*N

def to_num(c):
	return ord(c)-ord('a')

def to_char(n):
	return chr(n + ord('a'))

t = []
chars = [deque() for _ in range(26)]
l, r = 0, 0
for i in range(K):
	while r < N-K+1 + i:
		chars[to_num(S[r])].append(r)
		r += 1
	b = None
	for i, q in enumerate(chars):
		if q:
			t.append(i)
			b = q[0]
			break
	while l <= b:
		chars[to_num(S[l])].popleft()
		l += 1
	# print(list(map(list, chars)))

ans = "".join(map(to_char, t))
print(ans)
