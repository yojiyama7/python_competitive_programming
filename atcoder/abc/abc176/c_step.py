N = int(input())
A = list(map(int, input().split()))

sum_num = 0
b_max = 0
for a in A:
    # print(b_max, a)
    sum_num += max(b_max-a, 0)
    b_max = max(b_max, a)

print(sum_num)