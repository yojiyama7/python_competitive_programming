# まよいすぎ

N = int(input())

sum_num = 0
for i in range(1, 6):
    sum_num += max(0, N - 1000**i + 1)

print(sum_num)