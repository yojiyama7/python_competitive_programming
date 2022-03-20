def f(a):
    return int((a+1)*(a/2))

def sum_ab(a, b):
    return f(b) - f(a-1)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

sum_num = 0
for a, b in AB:
    sum_num += sum_ab(a, b)

print(sum_num)