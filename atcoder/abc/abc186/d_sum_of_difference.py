from itertools import accumulate as acc

N = int(input())
A = list(map(int, input().split()))

A.sort()
A_acc = [0] + list(acc(A))

sum_num = 0
for i, a in enumerate(A):
    sum_num += (A_acc[N] - A_acc[i+1]) - a * (N-i-1)

print(sum_num)
