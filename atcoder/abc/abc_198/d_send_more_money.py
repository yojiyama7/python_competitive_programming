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
