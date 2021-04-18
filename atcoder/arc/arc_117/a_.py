A, B = map(int, input().split())

e = list(range(-B, 0))
e += list(range(1, A+1))

sum_num = sum(e)
if sum_num < 0:
    e[-1] += abs(sum_num)
elif sum_num > 0:
    e[0] -= abs(sum_num)

print(*e)