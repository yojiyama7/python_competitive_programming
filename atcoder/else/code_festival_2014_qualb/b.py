N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

sum_num = 0
for i, a in enumerate(A):
    sum_num += a
    if sum_num >= K:
        print(i+1)
        break