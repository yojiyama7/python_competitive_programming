# 文字列操作って遅い？そりゃそうか
N = int(input())

def is_valid(digit):
	opened = 0
	for i in range(N):
		if (digit>>i)&1:
			opened += 1
		else:
			if opened <= 0:
				return False
			opened -= 1
	return opened == 0

l = []
for i in range(1<<N):
	if is_valid(i):
		t = ""
		for j in range(N):
			t += ")("[(i>>j)&1]
		l.append(t)

l.sort()
print(*l, sep='\n')
