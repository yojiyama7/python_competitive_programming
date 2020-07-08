N = int(input())

sum_num = 0
for i in range(1, N+1):
    if (i%3) and (i%5):
        sum_num += i

print(sum_num)