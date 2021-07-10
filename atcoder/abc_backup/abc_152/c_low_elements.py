N = int(input())
P = list(map(int, input().split()))

count = 0
min_num = 10**18
for p_i in P:
    min_num = min(min_num, p_i)
    if p_i <= min_num:
        count += 1

print(count)
