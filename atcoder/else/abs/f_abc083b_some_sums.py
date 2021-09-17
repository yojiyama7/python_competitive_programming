N, A, B = map(int, input().split())

count = 0
for i in range(1, N+1):
    if A <= sum(map(int, str(i))) <= B:
        count += i

print(count)