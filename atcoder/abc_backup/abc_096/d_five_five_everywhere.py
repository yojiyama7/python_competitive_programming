N = int(input())

x = []
p = []
for i in range(2, 2000):
    if all(i%p_i for p_i in p):
        p.append(i)
        if i%5 == 1:
            x.append(i)
            if len(x) == N:
                break

# print(*[x_i%5 for x_i in x])
print(*x)

# (5*?+1) (5*?+1) (5*?+1) (5*?+1) (5*?+1)
# 5*? + 5
# 5*(?+1)