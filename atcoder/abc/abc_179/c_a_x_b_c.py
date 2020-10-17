N = int(input())

cnt = 0
for i in range(1, N+1):
	# print(f"N以下の{i}の倍数: {(N-1)//i}")
	cnt += (N-1)//i

print(cnt)
