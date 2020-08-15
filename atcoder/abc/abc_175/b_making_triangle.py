N = int(input())
L = list(map(int, input().split()))

c = 0
for i, Li in enumerate(L):
    for j, Lj in enumerate(L):
        for k, Lk in enumerate(L):
            if i < j < k and len(set([Li, Lj, Lk])) == 3:
                max_e, *else_e = sorted([Li, Lj, Lk], reverse=True)
                if sum(else_e) > max_e:
                    c += 1

print(c)