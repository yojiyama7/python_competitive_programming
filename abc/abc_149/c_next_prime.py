from bisect import bisect_left

X = int(input())

p = [1]*(10**5+4)
for i in range(2, 10**5+4):
    if p[i]:
        for j in range(i*2, 10**5+4, i):
            # print(j)
            p[j] = 0

q = []
for i, p_i in enumerate(p):
    if p_i:
        q.append(i)

print(q[bisect_left(q, X)])
