from itertools import accumulate as acc

N = int(input())
A = list(map(int, input().split()))

l = acc(A)
q = []
s = 0
max_num = 0
for a in A:
    s += a
    max_num = max(s, max_num)
    q.append(max_num)

s = 0
max_num = 0
for i, l_i in enumerate(l):
    max_num = max(s + q[i], max_num)
    s += l_i

print(max_num)
