N = int(input())

cnt = 0
for i in range(1, N+1):
    if "7" in str(i) + oct(i):
        continue
    cnt += 1

print(cnt)
