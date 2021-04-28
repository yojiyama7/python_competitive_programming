def to_snake_case(s):
	l = []
	t = ""
	for c in s.lower():
		if c.isalnum():
			t += c
		elif t:
			l.append(t)
			t = ""
	if t:
		l.append(t)

	ans = '_'.join(l)
	return (ans)

S = input()

file_name = "_" + to_snake_case(S) + ".py"
with open(file_name, "w+", encoding="utf-8") as f:
	pass

