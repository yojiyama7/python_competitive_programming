N = int(input())
H = list(map(int, input().split()))

max_num = 0
count = 0
b = -(10**18)
for i, h in enumerate(H+[10**18]):
    # print(i, h, count)
    if h <= b:
        count += 1
    else:
        max_num = max(max_num, count)
        count = 0
    b = h

print(max_num)