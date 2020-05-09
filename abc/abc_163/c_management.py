N = int(input())
A = list(map(int, input().split()))

l = [0]*N
for a in A:
    l[a-1] += 1

for l_i in l:
    print(l_i)