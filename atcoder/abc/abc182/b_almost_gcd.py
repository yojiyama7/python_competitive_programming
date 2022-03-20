N = int(input())
A = list(map(int, input().split()))

max_num = 0
max_num_i = 1
for i in range(2, 1001):
    score = sum(a%i == 0 for a in A)
    if max_num < score:
        max_num = score
        max_num_i = i

print(max_num_i)