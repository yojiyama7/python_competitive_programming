N = int(input())

c = [[0 for _ in range(10)] for _ in range(10)]
for i in range(1, N+1):
    t = str(i)
    a, b = int(t[0]), int(t[-1])
    c[a][b] += 1

sum_num = 0
for s1 in range(10):
    for e1 in range(10):
        for s2 in range(10):
            for e2 in range(10):
                if s1 == e2 and e1 == s2:
                    sum_num += c[s1][e1] * c[s2][e2]

print(sum_num)