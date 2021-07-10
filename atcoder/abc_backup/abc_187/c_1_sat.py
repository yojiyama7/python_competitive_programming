N = int(input())
S = [input() for _ in range(N)]

d = dict()
for s in S:
	is_bikkuri = s[0] == "!"
	text = s[1:] if is_bikkuri else s
	if text not in d:
		d[text] = 0
	d[text] |= (1<<is_bikkuri)

# print(d)

for k, v in d.items():
	if v == 3:
		print(k)
		exit()
print("satisfiable")
