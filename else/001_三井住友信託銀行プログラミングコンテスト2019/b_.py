N = int(input())

l = []
for i in range(50001):
    l.append(int(i*1.08))

if N in l:
    print(l.index(N))
else:
    print(":(")