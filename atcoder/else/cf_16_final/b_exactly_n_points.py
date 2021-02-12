N = int(input())

sum_num = 0
length = -1
for i in range(1, N+1):
    sum_num += i
    if sum_num >= N:
        length = i
        break

l = []
for i in range(length, 0, -1):
    if i <= N:
        N -= i
        l.append(i)

print(*l, sep="\n")
