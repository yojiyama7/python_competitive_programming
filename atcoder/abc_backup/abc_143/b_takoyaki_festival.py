N = int(input())
D = list(map(int, input().split()))

sum_num = 0
for i, d1 in enumerate(D):
    for j, d2 in enumerate(D):
        if i < j:
            sum_num += d1*d2

print(sum_num)