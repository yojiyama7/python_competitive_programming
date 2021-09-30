N = int(input())

l = []
for i in range(0, 200, 20):
    x = list(range(20))
    # print(x[::-1])
    if (i//20)%2:
        l += x[::-1]
    else:
        l += x
    # print(l)
print(l[N-1]+1)
