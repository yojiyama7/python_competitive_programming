N = int(input())
A = [int(input()) for _ in range(N)]

sum_num = 0
cnt = 0
for i, a in enumerate(A, start=1):
    if a == 0:
        # print(i, sum_num, cnt//2)
        sum_num += cnt//2
        cnt = 0
        continue
    cnt += a
# print(i, sum_num, cnt//2)
sum_num += cnt//2

print(sum_num)
