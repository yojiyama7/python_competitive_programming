from itertools import permutations as perm
from math import factorial

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

all_sum = 0
for a in perm(XY):
    sum_num = 0
    for j in range(N-1):
        x1, y1 = a[j]
        x2, y2 = a[j+1]
        r = (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)
        sum_num += r
    all_sum += sum_num

print(all_sum / factorial(N))