# stack gaming

N = int(input())
S = input()

t = ""
stack = 0
for s in S:
	if s == "(":
		t += "("
		stack += 1
	else:
		t += ")"
		if stack:
			stack -= 1
		else:
			t = "(" + t
t += ")"*stack

print(t)

################################

# N = int(input())
# S = input()

# t = ""
# i = 0
# while (i < N):
# 	open_cnt = 0
# 	while (i < N and S[i] == "("):
# 		open_cnt += 1
# 		i += 1
# 	close_cnt = 0
# 	while (i < N and S[i] == ")"):
# 		close_cnt += 1
# 		i += 1
# 	size = max(open_cnt, close_cnt)
# 	t += "("*size + ")"*size

# print(t)
