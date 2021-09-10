N = int(input())
A = list(map(int, input().split()))

s = 0
max_num = -1
sum_num = 0
for i, a in enumerate(A, 1):
    s += sum_num
    s += a
    max_num = max(a, max_num)
    print(s + max_num*i)
    sum_num += a
