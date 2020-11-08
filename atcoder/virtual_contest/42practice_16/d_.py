N = int(input())
H = [int(input()) for _ in range(N)]

l = [H[i+1] - H[i] for i in range(N-1)]

i = 0
max_num = 1
while i < N-1:
    while i < N-1 and l[i] == 0:
        i += 1
    b = i
    while i < N-1 and l[i] > 0:
        i += 1
    while i < N-1 and l[i] < 0:
        i += 1
    max_num = max(i-b+1, max_num)

print(max_num)
