A, B, W = map(int, input().split())

first = None
last = None
for i in range(1000001):
    if A*i <= W*1000 <= B*i:
        if first == None:
            first = i
        last = i

if first:
    print(first, last)
else:
    print("UNSATISFIABLE")