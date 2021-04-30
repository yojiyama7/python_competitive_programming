# 枝刈り？
# TLEしない理由を知りたい

# from icecream import ic
# print = ic

N = int(input())
A, B, C = map(int, input().split())

def solve():
	min_num = 9999
	for i in range(10000):
		if A*i > N:
			break
		for j in range(10000-i):
			if A*i + B*j > N:
				break
			remain = N - (A*i + B*j)
			# print(remain)
			if remain%C:
				continue
			k = remain//C
			# print(i, j, k)
			min_num = min(
				i+j+k,
				min_num
			)
	return (min_num)

print(solve())
