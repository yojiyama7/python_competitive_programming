# pypy AC
# python TLE

from itertools import permutations as permut

S = S1, S2, S3 = [input() for _ in range(3)]

chars = list(set("".join(S)))
chars_len = len(chars)
if chars_len > 10:
	print("UNSOLVABLE")
	exit()

def convert(t, d):
	return [d[t_i] for t_i in t]

def to_int(l):
	x = 0
	for l_i in l:
		x *= 10
		x += l_i
	return x

# key を int にしとくと軽い
d = dict(zip(chars, range(chars_len)))
t1 = convert(S1, d)
t2 = convert(S2, d)
t3 = convert(S3, d)
for l in permut(range(10), chars_len):
	# key を int にしとくと軽い
	a = convert(t1, l)
	b = convert(t2, l)
	c = convert(t3, l)
	if a[0] == 0 or b[0] == 0 or c[0] == 0:
		continue
	a, b, c = to_int(a), to_int(b), to_int(c)
	if a+b == c:
		print(a)
		print(b)
		print(c)
		exit()

print("UNSOLVABLE")

################################

# # TLE

# # str -> int の変換をするような実装 遅い
# # 数字からの方がいい

# from itertools import permutations as permut

# S = S1, S2, S3 = [input() for _ in range(3)]

# chars = list(set("".join(S)))
# chars_len = len(chars)
# if chars_len > 10:
# 	print("UNSOLVABLE")
# 	exit()

# def convert(t, d):
# 	return [d[t_i] for t_i in t]

# def to_int(l):
# 	x = 0
# 	for l_i in l:
# 		x *= 10
# 		x += l_i
# 	return x

# # key を int にしとくと軽い？
# for l in permut(range(10), chars_len):
# 	# key を int にしとくと軽い？
# 	d = dict(zip(chars, l))
# 	a = convert(S1, d)
# 	b = convert(S2, d)
# 	c = convert(S3, d)
# 	if a[0] == 0 or b[0] == 0 or c[0] == 0:
# 		continue
# 	a, b, c = to_int(a), to_int(b), to_int(c)
# 	if a+b == c:
# 		print(a)
# 		print(b)
# 		print(c)
# 		exit()

# print("UNSOLVABLE")

################################

# # TLE

# from itertools import permutations as perm

# S1 = input()
# S2 = input()
# S3 = input()

# chars = list(set(S1) | set(S2) | set(S3))
# if len(chars) > 10:
# 	print("UNSOLVABLE")
# 	exit()

# def to_int(s, table):
# 	x = 0
# 	for s_i in s:
# 		x *= 10
# 		x += table[s_i]
# 	return x

# starts = [S1[0], S2[0], S3[0]]
# for nums in perm(range(10), len(chars)):
# 	# print(nums)
# 	table = dict()
# 	for j in range(len(chars)):
# 		table[chars[j]] = nums[j]
# 	if table[S1[0]] == 0 or table[S2[0]] == 0 or table[S3[0]] == 0:
# 		continue
# 	a = to_int(S1, table)
# 	b = to_int(S2, table)
# 	c = to_int(S3, table)
# 	if a + b == c:
# 		print(a)
# 		print(b)
# 		print(c)
# 		exit()
# 		# break

# print("UNSOLVABLE")
