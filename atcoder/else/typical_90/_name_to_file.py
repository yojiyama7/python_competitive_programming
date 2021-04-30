def pattern(c):
	if c.isalpha():
		return 0
	if c.isdigit():
		return 1
	return 2

def to_snake_case(s):
	l = []
	t = ""
	b = -1
	for c in s.lower():
		if pattern(c) == 2 or b != pattern(c):
			if t:
				l.append(t)
			t = ""
		if pattern(c) in [0, 1]:
			t += c
		b = pattern(c)
	if t:
		l.append(t)

	ans = '_'.join(l)
	return (ans)

S = input()

file_name = "_" + to_snake_case(S) + ".py"
with open(file_name, "w+", encoding="utf-8") as f:
	pass

