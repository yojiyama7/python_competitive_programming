N = int(input())
X = list(map(int, input().split()))

min_num = 10**18
for i in range(1, 101):
    m = sum((x-i)**2 for x in X)
    min_num = min(min_num, m)

print(min_num)