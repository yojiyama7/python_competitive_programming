N = int(input())
X = list(map(int, input()))
# N = 2*10**5
# X = list(map(int, "10"*(N//2)))

Xp = sum(X)
        
# print(Xp)
a = 0
b = 0
# c = 0
# :N
for i, x in enumerate(X):
    i_reverse = N-i-1
    if Xp > 1:
        a = (a + x * pow(2, i_reverse, Xp-1)) % (Xp-1)
    b = (b + x * pow(2, i_reverse, Xp+1)) % (Xp+1)
    # c = (c + x * (1<<i_reverse))
    # print(bin(c))

# print(a, b)

# :N
for i in range(N):
    i_reverse = N-i-1
    if Xp > 1:
        m = ([a, b][X[i]==0] + [-1, 1][X[i]==0] * pow(2, i_reverse, [Xp-1, Xp+1][X[i]==0])) % [Xp-1, Xp+1][X[i]==0]
    else:
        if X[i]==0:
            m = (b + pow(2, i_reverse, Xp+1)) % (Xp+1)
        else:
            print(0)
            continue
    count = 1
    # print(i, ([a, b][X[i]==0], [-1, 1][X[i]==0]*(1<<i_reverse)), [Xp-1, Xp+1][X[i]==0], X[i]==0)
    # print(m)
    while m > 0:
        p = sum([int(c) for c in str(bin(m)[2:])])
        m = m % p
        count += 1
    print(count)
