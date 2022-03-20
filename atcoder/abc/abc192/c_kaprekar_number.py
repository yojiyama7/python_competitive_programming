Iints = lambda: list(map(int, input().split()))

N, K = Iints()

g1 = lambda x: int("".join(sorted(str(x), reverse=True)))
g2 = lambda x: int("".join(sorted(str(x))))
f = lambda x: g1(x) - g2(x)

a = [N]
for i in range(1, K+1):
    a.append(f(a[i-1]))

print(a[K])
