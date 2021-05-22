from math import factorial as fact

A, B, K = map(int, input().split())

# 'a'をa個, 'b'をb個使ってできる長さ a+b の文字列の個数は
# a+b C a

def combi(n, k):
	if n < 0 or k < 0 or n < k:
		return 0
	# 割り切れ！！！
	return fact(n)//fact(k)//fact(n-k)

# def solve(a, b, idx):
# 	if a == b == 0:
# 		return ''
# 	a_cnt = combi(a+b-1, a-1) if a else 0
# 	if idx < a_cnt:
# 		return 'a' + solve(a-1, b, idx)
# 	else:
# 		return 'b' + solve(a, b-1, idx-a_cnt)
# ans = solve(A, B, K-1)
# print(ans)

a, b = A, B
idx = K-1
t = ""
for i in range(A+B):
	# A+B-i文字で構成される文字列のうちaで始まるものは a_cnt 通りある
	# combi(a+b-1, b-1) == combi(a+b, a) - a_cnt
	a_cnt = combi(a+b-1, a-1)
	# if not (combi(a+b-1, b-1) == combi(a+b, a) - a_cnt):
	# 	print("?")
	if idx < a_cnt:
		t += 'a'
		a -= 1
	else:
		t += 'b'
		b -= 1
		idx -= a_cnt
print(t)
