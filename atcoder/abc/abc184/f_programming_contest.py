from bisect import bisect_right

N, T = map(int, input().split())
A = list(map(int, input().split()))
# N, T = 40, 10**9
# A = [(10**8 + 2**i)%(10**9) for i in range(N)]

a = A[:N//2]
b = A[N//2:]

a_sums = []
length = N//2
for i in range(1<<length):
    sum_num = 0
    for j in range(length):
        if i&(1<<j):
            sum_num += a[j]
    a_sums.append(sum_num)

b_sums = []
length = N - N//2
for i in range(1<<length):
    sum_num = 0
    for j in range(length):
        if i&(1<<j):
            sum_num += b[j]
    b_sums.append(sum_num)
b_sums.sort()

# print(a_sums, b_sums)

max_score = 0
for ai in a_sums:
    remain = T - ai
    if remain < 0:
        continue
    # print(ai, remain, b_sums[bisect_right(b_sums, remain)-1])
    bi = b_sums[bisect_right(b_sums, remain)-1]
    score = ai + bi
    max_score = max(max_score, score)

print(max_score)