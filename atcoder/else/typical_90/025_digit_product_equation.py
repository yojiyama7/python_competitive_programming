# f(x) が同じものを同一視で全探索
# 言われてみればなという感じ
# 詰め甘死 最近これすぎる 集中できてない

# from collections import Counter
# import sys
# sys.setrecursionlimit(10**8)

# N, B = map(int, input().split())

# def f(x):
# 	ans = 1
# 	for y in map(int, str(x)):
# 		ans *= y
# 	return ans

# def dfs(s, before):
# 	if len(s) == 11:
# 		t = f(int(s)) + B
# 		u = '0'*(11-len(str(t))) + ''.join(sorted(str(t)))
# 		if not (u == s):
# 			return False
# 		print(s, t, "aa")
# 		if t > N:
# 			return False
# 		return True
# 	cnt = 0
# 	for i in range(before, 10):
# 		cnt += dfs(s+str(i), i)
# 	return (cnt)

# ans = dfs("", 0)
# print(ans)

################################

# # 考察してみたものの うーんという感じ
# # 桁dp的に考えれるのか
# # 数学で殴る式変形なのか
# # その他ひらめきなのかという感じ
# # 答えを見てみる

# def f(x):
# 	ans = 1
# 	for y in map(int, str(x)):
# 		ans *= y
# 	return ans

# for i in range(100):
# 	print(i, f(i), i-f(i))

# # N, B = map(int, input().split())
