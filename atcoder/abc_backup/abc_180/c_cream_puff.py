N = int(input())

l = []
i = 1
while i**2 <= N:
    if N%i == 0:
        l.append(i)
        l.append(N//i)
    i+=1

l = sorted(list(set(l)))

[print(l_i) for l_i in l]